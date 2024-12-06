from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "InsulatedJoint"
imx_version = ImxVersionEnum.v124

insulated_joint_entities_v124 = [
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="InsulatedJoint",
        properties={},
        icon_groups=[
            IconSvgGroup("insulatedJoint"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="InsulatedJointLeft",
        properties={"rail": "LeftRail"},
        icon_groups=[
            IconSvgGroup("insulatedJoint"),
            IconSvgGroup("insulatedJoint-left"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="InsulatedJointRight",
        properties={"rail": "RightRail"},
        icon_groups=[
            IconSvgGroup("insulatedJoint"),
            IconSvgGroup("insulatedJoint-right"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="InsulatedJointBoth",
        properties={"rail": "Both"},
        icon_groups=[
            IconSvgGroup("insulatedJoint"),
            IconSvgGroup("insulatedJoint-left"),
            IconSvgGroup("insulatedJoint-right"),
        ],
    ),
]
