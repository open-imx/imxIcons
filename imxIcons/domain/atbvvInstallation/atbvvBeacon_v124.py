from imxIcons.domain.helpers import copy_icon_and_assign_imx_path
from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "ATBVVInstallation.ATBVVBeacon"
imx_version = ImxVersionEnum.v124

atb_vv_beacon_entities_v124 = [
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="ATBVVBeacon",
        properties={},
        icon_groups=[
            IconSvgGroup("atbVv-Beacon"),
        ],
    )
]

atb_vv_beacon_entities_v124_no_path = copy_icon_and_assign_imx_path(
    "ATBVVBeacon", atb_vv_beacon_entities_v124
)
