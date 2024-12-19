from imxIcons.domain.helpers import copy_icon_and_assign_imx_path
from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "Signal.ReflectorPost"
imx_version = ImxVersionEnum.v500


reflector_post_icon_entities_v500 = [
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="ReflectorPostStraight",
        properties={"reflectorType": "Straight"},
        icon_groups=[
            IconSvgGroup("signal-reflector-straight"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="ReflectorPostDiagonal",
        properties={"reflectorType": "Diagonal"},
        icon_groups=[
            IconSvgGroup("signal-reflector-diagonal"),
        ],
    ),
]

reflector_post_icon_entities_v500_no_path = copy_icon_and_assign_imx_path(
    "ReflectorPost", reflector_post_icon_entities_v500
)
