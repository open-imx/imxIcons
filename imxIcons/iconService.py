import re
from typing import Any, cast

from lxml import etree
from lxml.etree import XMLParser

from imxIcons.domain.icon_library import ICON_DICT  # DEFAULT_ICONS
from imxIcons.domain.supportedIconTypes import IconTypesEnum, icon_types_literal
from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.domain.svg_data import (
    QGIS_SVG_GROUP_DICT,
    QGIS_SVG_GROUP_DICT_DARK,
    SVG_SVG_GROUP_DICT,
    SVG_SVG_GROUP_DICT_DARK,
)
from imxIcons.iconEntity import IconEntity, IconSvgGroup
from imxIcons.iconServiceModels import IconRequestModel


class IconService:
    """Service for handling and generating SVG icons."""

    @staticmethod
    def _add_transform_to_groups(svg_groups: list[str]) -> list[str]:
        """
        Adds a transform attribute to a list of SVG group strings.

        Args:
            svg_groups: A list of SVG group strings.

        Returns:
            A list of SVG groups with a transform attribute added.
        """
        updated_groups = []

        for group in svg_groups:
            updated_group = re.sub(
                r'(<g\s+id="[^"]*")', r'\1 transform="translate(25, 25)"', group
            )
            updated_groups.append(updated_group)

        return updated_groups

    @staticmethod
    def _add_transform_to_elements(svg_str: str, transform_str: str) -> str:
        """
        Adds a transform attribute to geometry elements in an SVG string.

        Args:
            svg_str: The input SVG string.
            transform_str: The transformation string to apply.

        Returns:
            A modified SVG string with the transformation applied to geometry elements.
        """
        if transform_str is None:
            return svg_str  # pragma: no cover

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
        """
        Formats an SVG string to be pretty-printed.

        Args:
            svg_str: The input SVG string.

        Returns:
            A pretty-printed SVG string.
        """
        parser = XMLParser(remove_blank_text=True)
        root = etree.fromstring(svg_str, parser)
        return etree.tostring(root, encoding="unicode", pretty_print=True)

    @staticmethod
    def _clean_key(key: str) -> str:
        """
        Cleans a key by removing leading '@' characters from each part of a dotted key string.

        Args:
            key: The key string to clean.

        Returns:
            A cleaned version of the key.
        """
        return ".".join(part.lstrip("@") for part in key.split("."))

    @classmethod
    def _get_svg_name_and_groups(
        cls, entry: dict[str, Any], subtypes: list[IconEntity]
    ) -> tuple[Any, list[IconSvgGroup]]:
        """
        Retrieves the SVG name and groups that match the properties in an entry.

        Args:
            entry: The entry dictionary containing properties.
            subtypes: A list of IconEntity objects representing subtypes.

        Returns:
            A tuple containing the icon name and the matching SVG groups.

        Raises:
            NotImplementedError: If no matching subtypes are found.
        """
        matching_subtypes: list[tuple[int, str, IconEntity]] = []
        if entry.get("additional_properties", {}):
            entry_properties = entry.get("properties", {}) | entry.get(
                "additional_properties", {}
            )
        else:
            entry_properties = entry.get("properties", {})

        entry_properties = {
            cls._clean_key(key): value for key, value in entry_properties.items()
        }

        entry_keys = {key for key, value in entry_properties.items() if value != ""}

        for details in subtypes:
            subtype_properties = details.properties | details.additional_properties
            subtype_keys = set(subtype_properties)

            if not subtype_keys.issubset(entry_keys):
                continue

            if all(
                (entry_properties.get(key) == value or "*" == value)
                for key, value in subtype_properties.items()
            ):
                matching_subtypes.append(
                    (len(subtype_keys), details.icon_name, details)
                )

        sorted_matching_subtypes = sorted(
            matching_subtypes, key=lambda x: x[0], reverse=True
        )

        if len(sorted_matching_subtypes) == 0:
            # TODO: if len is 0, else return default icon for path
            raise NotImplementedError(
                "No default icons are implemented"
            )  # pragma: no cover

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
        """
        Retrieves the icon name for a given request model and IMX version.

        Args:
            request_model: The request model containing icon path and properties.
            imx_version: The IMX version to match.

        Returns:
            The name of the matching icon.

        Raises:
            ValueError: If no icon is found for the combination of IMX path and version.
        """
        try:
            imx_path_icons = ICON_DICT[request_model.imx_path][imx_version.name]
        except Exception:  # pragma: no cover
            raise ValueError(  # noqa: TRY003 pragma: no cover
                "combination of imx path and imx version do not have a icon in the library"
            )

        icon_name, svg_groups = cls._get_svg_name_and_groups(
            dict(request_model), imx_path_icons
        )
        return icon_name

    @classmethod
    def _create_svg(
        cls,
        imx_path: str,
        icon_name: str,
        svg_groups: list[IconSvgGroup],
        icon_type: IconTypesEnum | icon_types_literal,
    ):
        """
        Creates an SVG string from icon details and SVG groups.

        Args:
            imx_path: The IMX path for the icon.
            icon_name: The name of the icon.
            svg_groups: A list of SVG groups associated with the icon.
            icon_type: If True, a qgis svg will be returned

        Returns:
            An SVG string for the icon.
        """
        if isinstance(icon_type, str):
            icon_type = IconTypesEnum.from_string(icon_type)
        icon_type = cast(IconTypesEnum, icon_type)

        icon_type_mapping = {
            IconTypesEnum.qgis.name: QGIS_SVG_GROUP_DICT,
            IconTypesEnum.qgis_dark.name: QGIS_SVG_GROUP_DICT_DARK,
            IconTypesEnum.svg_dark.name: SVG_SVG_GROUP_DICT_DARK,
        }
        icon_dict = icon_type_mapping.get(icon_type.name, SVG_SVG_GROUP_DICT)

        svg_groups_str = [
            cls._add_transform_to_elements(
                icon_dict[item.group_id], item.transform or ""
            )
            for item in svg_groups
        ]
        group_data = "\n".join(cls._add_transform_to_groups(svg_groups_str))
        svg_content = f"""
        <svg xmlns="http://www.w3.org/2000/svg" name="{icon_name}" class="svg-colored" width="250" height="250" viewBox="0 0 50 50">
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
        icon_type: IconTypesEnum | icon_types_literal = IconTypesEnum.svg,
    ) -> dict[str, dict[str, str | dict[str, str]]]:
        """
        Retrieves all icons for a given IMX version.

        Args:
            imx_version: The IMX version to match.
            icon_type: If True, a qgis svg will be returned

        Returns:
            A dictionary of icon names and their corresponding SVG content and metadata.

        Raises:
            ValueError: If no icons are found for the IMX version.
        """
        try:
            imx_path_icons = {
                key: value[imx_version.name] for key, value in ICON_DICT.items()
            }
        except Exception:  # pragma: no cover
            raise ValueError(  # noqa: TRY003 pragma: no cover
                "combination of imx path and imx version do not have a icon in the library"
            )
        out = {}
        for imx_type, icons in imx_path_icons.items():
            for icon_entity in icons:
                svg_content = cls._create_svg(
                    icon_entity.imx_path,
                    icon_entity.icon_name,
                    icon_entity.icon_groups,
                    icon_type,
                )
                out[icon_entity.icon_name] = {
                    "imx_version": icon_entity.imx_version.name,
                    "imx_path": icon_entity.imx_path,
                    "imx_properties": icon_entity.properties,
                    "imx_additional_properties": icon_entity.additional_properties,
                    "icon": svg_content.strip(),
                }
        return out

    @classmethod
    def get_svg(
        cls,
        request_model: IconRequestModel,
        imx_version: ImxVersionEnum,
        pretty_svg: bool = True,
        icon_type: IconTypesEnum | icon_types_literal = IconTypesEnum.svg,
    ) -> Any:
        """
        Retrieves the SVG content for a given request model and IMX version.

        Args:
            request_model: The model containing icon request details such as the IMX path and properties.
            imx_version: The IMX version to match for retrieving the icon.
            pretty_svg: If True, formats the SVG content for pretty printing.
            icon_type: If True, a qgis svg will be returned

        Returns:
            The SVG content as a string. If `pretty_svg` is True, the SVG is formatted for better readability.

        Raises:
            ValueError: If no icon is found for the combination of IMX path and version.
        """
        try:
            imx_path_icons = ICON_DICT[request_model.imx_path][imx_version.name]
        except Exception:  # pragma: no cover
            raise ValueError(  # noqa: TRY003 pragma: no cover
                "combination of imx path and imx version do not have a icon in the library"
            )

        icon_name, svg_groups = cls._get_svg_name_and_groups(
            dict(request_model), imx_path_icons
        )
        svg_content = cls._create_svg(
            request_model.imx_path, icon_name, svg_groups, icon_type
        )

        if pretty_svg:
            return cls._format_svg(svg_content.strip())
        return svg_content
