from imxIcons.domain.helpers import copy_icon_and_assign_imx_path
from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "AtbVvInstallation.AtbVvBeacon"
imx_version = ImxVersionEnum.v500

atb_vv_beacon_entities_v500 = [
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

atb_vv_beacon_entities_v500_no_path = copy_icon_and_assign_imx_path(
    "AtbVvBeacon", atb_vv_beacon_entities_v500
)
