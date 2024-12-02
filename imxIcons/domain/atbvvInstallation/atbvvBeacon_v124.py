from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "ATBVVBeacon"
imx_version = ImxVersionEnum.v124

atbvv_beacon_entities_v124 = [
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="ATBVVBeacon",
        properties={},
        icon_groups=[
            IconSvgGroup("atbvvBeacon"),
        ],
    )
]
