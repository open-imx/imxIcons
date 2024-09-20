import re
from typing import Any

from lxml import etree
from lxml.etree import XMLParser

from imxIcons.domain import ICON_DICT  # DEFAULT_ICONS
from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.domain.svg_data import SVG_ICON_DICT
from imxIcons.iconEntity import IconSvgGroup
from imxIcons.iconServiceModels import IconRequestModel


class IconService:
    @staticmethod
    def add_transform_to_groups(svg_groups):
        updated_groups = []

        for group in svg_groups:
            updated_group = re.sub(
                r'(<g\s+id="[^"]*")', r'\1 transform="translate(25, 25)"', group
            )
            updated_groups.append(updated_group)

        return updated_groups

    @staticmethod
    def add_transform_to_elements(svg_str, transform_str):
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
    def format_svg(svg_str):
        parser = XMLParser(remove_blank_text=True)
        root = etree.fromstring(svg_str, parser)
        return etree.tostring(root, encoding="unicode", pretty_print=True)

    @staticmethod
    def _clean_key(key):
        return ".".join(part.lstrip("@") for part in key.split("."))

    @classmethod
    def get_svg_name_and_groups(cls, entry, subtypes) -> list[list[IconSvgGroup]]:
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
            # todo: if len is 0, else return default icon for path
            raise NotImplementedError("No default icons are implemented")

        return [
            sorted_matching_subtypes[0][1],
            sorted_matching_subtypes[0][2].icon_groups,
        ]

    @classmethod
    def get_svg(
        cls,
        request_model: IconRequestModel,
        imx_version: ImxVersionEnum,
        pretty_svg=True,
    ) -> Any:
        try:
            imx_path_icons = ICON_DICT[request_model.imx_path][imx_version.name]
        except Exception:
            raise ValueError(  # noqa: TRY003
                "combination of imx path and imx version do not have a icon in the library"
            )

        icon_name, svg_groups = cls.get_svg_name_and_groups(
            dict(request_model), imx_path_icons
        )

        svg_groups = [
            cls.add_transform_to_elements(SVG_ICON_DICT[item.group_id], item.transform)
            for item in svg_groups
        ]

        # we all so should return
        #   - the svg groups so we can have badges
        #   - add center point to image.

        group_data = "\n".join(cls.add_transform_to_groups(svg_groups))

        svg_content = f"""
        <svg xmlns="http://www.w3.org/2000/svg" name="{icon_name}" class="svg-colored" viewBox="0 0 50 50">
            <g class="open-imx-icon {request_model.imx_path}" transform="translate(25, 25)">
               {group_data}
            </g>
        </svg>

        """

        if pretty_svg:
            return cls.format_svg(svg_content.strip())
        return svg_content
