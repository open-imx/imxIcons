from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "AxleCounterDetectionPoint"
imx_version = ImxVersionEnum.v500

axle_counter_points_icon_entities_v500 = [
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
