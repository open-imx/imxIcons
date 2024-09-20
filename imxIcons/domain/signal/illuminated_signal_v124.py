from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "Signal.IlluminatedSign"
imx_version = ImxVersionEnum.v124


illuminated_signs = [
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="IlluminatedSignIntegrated",
        properties={"isIntegrated": "True"},
        icon_groups=[
            IconSvgGroup("illuminated-sign-integrated", "translate(7.25, 0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="IlluminatedSignNotIntegrated",
        properties={"isIntegrated": "False"},
        icon_groups=[
            IconSvgGroup("illuminated-sign-not-integrated"),
        ],
    ),
]


illuminated_sign_icon_entities_v124 = illuminated_signs
