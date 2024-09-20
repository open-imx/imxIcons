from copy import deepcopy
from dataclasses import dataclass

from imxIcons.domain.supportedImxVersions import ImxVersionEnum


@dataclass
class IconSvgGroup:
    group_id: str
    transform: str | None = None


@dataclass
class IconEntity:
    imx_version: ImxVersionEnum
    imx_path: str
    icon_name: str
    properties: dict[str, str]
    icon_groups: list[IconSvgGroup]

    def extend_icon(
        self, name: str, extra_props: dict[str, str], extra_groups: list[IconSvgGroup]
    ):
        _ = deepcopy(self)
        _.icon_name = name
        _.properties = _.properties | extra_props
        _.icon_groups.extend(extra_groups)
        return _
        pass
