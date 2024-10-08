import re
from typing import Any

from lxml import etree
from lxml.etree import XMLParser

from imxIcons.domain import ICON_DICT  # DEFAULT_ICONS
from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.domain.svg_data import SVG_ICON_DICT
from imxIcons.iconEntity import IconEntity, IconSvgGroup
from imxIcons.iconServiceModels import IconRequestModel


class IconService:
    @staticmethod
    def _add_transform_to_groups(svg_groups: list[str]) -> list[str]:
        updated_groups = []

        for group in svg_groups:
            updated_group = re.sub(
                r'(<g\s+id="[^"]*")', r'\1 transform="translate(25, 25)"', group
            )
            updated_groups.append(updated_group)

        return updated_groups

    @staticmethod
    def _add_transform_to_elements(svg_str: str, transform_str: str) -> str:
        if transform_str is None:
            return svg_str

        root = etree.fromstring(svg_str)
        geometry_elements = [
            "circle",
            "line",
            "rect",
            "ellipse",
            "polygon",
            "polyline",
            "path",
        ]
        for element in root:
            if element.tag in geometry_elements:
                element.set("transform", transform_str)
        return etree.tostring(root, encoding="unicode")

    @staticmethod
    def _format_svg(svg_str: str) -> str:
        parser = XMLParser(remove_blank_text=True)
        root = etree.fromstring(svg_str, parser)
        return etree.tostring(root, encoding="unicode", pretty_print=True)

    @staticmethod
    def _clean_key(key: str) -> str:
        return ".".join(part.lstrip("@") for part in key.split("."))

    @classmethod
    def get_svg_name_and_groups(
        cls, entry: dict[str, Any], subtypes: list[IconEntity]
    ) -> tuple[Any, list[IconSvgGroup]]:
        matching_subtypes = []
        entry_properties = entry.get("properties", {})

        entry_properties = {
            cls._clean_key(key): value for key, value in entry_properties.items()
        }

        entry_keys = set(entry_properties)

        for details in subtypes:
            subtype_properties = details.properties
            subtype_keys = set(subtype_properties)

            if not subtype_keys.issubset(entry_keys):
                continue

            if all(
                (entry_properties.get(key) == value or "*" == value)
                for key, value in subtype_properties.items()
            ):
                matching_subtypes.append(
                    [len(subtype_keys), details.icon_name, details]
                )

        sorted_matching_subtypes = sorted(
            matching_subtypes, key=lambda x: x[0], reverse=True
        )

        if len(sorted_matching_subtypes) == 0:
            # TODO: if len is 0, else return default icon for path
            raise NotImplementedError("No default icons are implemented")  # pragma: no cover

        return (
            sorted_matching_subtypes[0][1],
            sorted_matching_subtypes[0][2].icon_groups,
        )

    @classmethod
    def get_icon_name(
        cls,
        request_model: IconRequestModel,
        imx_version: ImxVersionEnum,
    ) -> str:
        try:
            imx_path_icons = ICON_DICT[request_model.imx_path][imx_version.name]
        except Exception:  # pragma: no cover
            raise ValueError(  # noqa: TRY003 pragma: no cover
                "combination of imx path and imx version do not have a icon in the library"
            )

        icon_name, svg_groups = cls.get_svg_name_and_groups(
            dict(request_model), imx_path_icons
        )
        return icon_name

    @classmethod
    def _create_svg(cls, imx_path: str, icon_name: str, svg_groups: list[IconSvgGroup]):
        svg_groups = [
            cls._add_transform_to_elements(SVG_ICON_DICT[item.group_id], item.transform)
            for item in svg_groups
        ]
        group_data = "\n".join(cls._add_transform_to_groups(svg_groups))
        svg_content = f"""
        <svg xmlns="http://www.w3.org/2000/svg" name="{icon_name}" class="svg-colored" viewBox="0 0 50 50">
            <g class="open-imx-icon {imx_path}" transform="translate(25, 25)">
               {group_data}
            </g>
        </svg>
        """
        return svg_content

    @classmethod
    def get_all_icons(
        cls,
        imx_version: ImxVersionEnum,
    ) -> dict[str, dict[str, str | dict[str, str]]]:
        try:
            imx_path_icons = {
                key: value[imx_version.name] for key, value in ICON_DICT.items()
            }
        except Exception: # pragma: no cover
            raise ValueError(  # noqa: TRY003 pragma: no cover
                "combination of imx path and imx version do not have a icon in the library"
            )
        out = {}
        for imx_type, icons in imx_path_icons.items():
            for icon_entity in icons:
                svg_content = cls._create_svg(
                    icon_entity.imx_path, icon_entity.icon_name, icon_entity.icon_groups
                )
                out[icon_entity.icon_name] = {
                    "imx_version": icon_entity.imx_version.name,
                    "imx_path": icon_entity.imx_path,
                    "imx_properties": icon_entity.properties,
                    "icon": svg_content.strip(),
                }
        return out


    @classmethod
    def get_svg(
        cls,
        request_model: IconRequestModel,
        imx_version: ImxVersionEnum,
        pretty_svg=True,
    ) -> Any:
        try:
            imx_path_icons = ICON_DICT[request_model.imx_path][imx_version.name]
        except Exception:  # pragma: no cover
            raise ValueError(  # noqa: TRY003 pragma: no cover
                "combination of imx path and imx version do not have a icon in the library"
            )

        icon_name, svg_groups = cls.get_svg_name_and_groups(
            dict(request_model), imx_path_icons
        )
        svg_content = cls._create_svg(request_model.imx_path, icon_name, svg_groups)

        if pretty_svg:
            return cls._format_svg(svg_content.strip())
        return svg_content
