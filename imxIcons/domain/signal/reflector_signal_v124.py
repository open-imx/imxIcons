from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "Signal.ReflectorPost"
imx_version = ImxVersionEnum.v124


reflector_posts = [
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
        icon_name="IlluminatedSignNotIntegrated",
        properties={"reflectorType": "diagonal"},
        icon_groups=[
            IconSvgGroup("signal-reflector-diagonal"),
        ],
    ),
]

reflector_post_icon_entities_v124 = reflector_posts
