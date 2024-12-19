from imxIcons.domain.helpers import copy_icon_and_assign_imx_path
from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "Signal.ReflectorPost"
imx_version = ImxVersionEnum.v124


reflector_post_icon_entities_v124 = [
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="ReflectorPostStraight",
        properties={"reflectorType": "straight"},
        icon_groups=[
            IconSvgGroup("signal-reflector-straight"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="ReflectorPostDiagonal",
        properties={"reflectorType": "diagonal"},
        icon_groups=[
            IconSvgGroup("signal-reflector-diagonal"),
        ],
    ),
]

reflector_post_icon_entities_v124_no_path = copy_icon_and_assign_imx_path(
    "ReflectorPost", reflector_post_icon_entities_v124
)
