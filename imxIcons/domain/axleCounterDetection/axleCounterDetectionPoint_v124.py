from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "AxleCounterDetectionPoint"
imx_version = ImxVersionEnum.v124

axle_counter_points_icon_entities_v124 = [
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="AxleCounterDetectionPoint",
        properties={},
        icon_groups=[
            IconSvgGroup("axleCounter-base"),
        ],
    )
]
