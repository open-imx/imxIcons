from copy import deepcopy
from dataclasses import dataclass

from imxIcons.domain.supportedImxVersions import ImxVersionEnum


@dataclass
class IconSvgGroup:
    """
    Represents a group of SVG elements within an icon.

    Attributes:
        group_id: A unique identifier for the SVG group.
        transform: A transformation string to apply to the SVG group (e.g., translation, scaling).
    """

    group_id: str
    transform: str | None = None


@dataclass
class IconEntity:
    """
    Represents an icon entity with metadata, properties, and SVG groups.

    Attributes:
        imx_version: The version of the IMX format this icon is based on.
        imx_path: The file path to the IMX data.
        icon_name: The name of the icon.
        properties: A dictionary of additional properties for the icon.
        icon_groups: A list of groups representing the SVG structure of the icon.
    """

    imx_version: ImxVersionEnum
    imx_path: str
    icon_name: str
    properties: dict[str, str]
    icon_groups: list[IconSvgGroup]

    def extend_icon(
        self, name: str, extra_props: dict[str, str], extra_groups: list[IconSvgGroup]
    ):
        """
        Creates a new icon entity based on the current one with additional properties
        and groups, and a different icon name.

        Args:
            name: The new name for the icon.
            extra_props: Additional properties to be added to the icon.
            extra_groups: Additional SVG groups to be added to the icon.

        Returns:
            A new `IconEntity` with updated properties and groups.
        """
        _ = deepcopy(self)
        _.icon_name = name
        _.properties = _.properties | extra_props
        _.icon_groups.extend(extra_groups)
        return _
        pass
