from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "LevelCrossing"
imx_version = ImxVersionEnum.v500


level_crossing_entities_v500 = [
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="LevelCrossing",
        properties={},
        icon_groups=[
            IconSvgGroup("levelCrossing"),
        ],
    )
]
