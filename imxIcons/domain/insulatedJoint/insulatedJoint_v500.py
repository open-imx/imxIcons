from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "InsulatedJoint"
imx_version = ImxVersionEnum.v500

insulated_joint_entities_v500 = [
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="InsulatedJoint",
        properties={},
        icon_groups=[
            IconSvgGroup("insulatedJoint"),
        ],
    )
]
