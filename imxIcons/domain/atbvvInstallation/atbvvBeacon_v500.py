from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "AtbVvInstallation.AtbVvBeacon"
imx_version = ImxVersionEnum.v500

atbvv_beacon_entities_v500 = [
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="AtbVvBeacon",
        properties={},
        icon_groups=[
            IconSvgGroup("atbVv-Beacon"),
        ],
    )
]
