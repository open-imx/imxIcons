from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "SpeedSign"
imx_version = ImxVersionEnum.v124


def add_arrow_marker(sign):
    temp_list = []
    for item in sign:
        translate = (
            "translate(-2.5, -1.15)"
            if "Low" in item.icon_name
            else "translate(-4, -1.15)"
        )
        temp_list.append(
            item.extend_icon(
                name=item.icon_name + "ArrowRight",
                extra_props={"hasArrowMarker": "True"},
                extra_groups=[IconSvgGroup("arrow-sign", f"rotate(180), {translate}")],
            )
        )
    sign.extend(temp_list)


signs = [
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS314",
        properties={
            "speedSignType": "MaximumSpeed",
            "signalPosition": "High",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("RS-314", "translate(6.5, 0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS314Bis",
        properties={
            "speedSignType": "MaximumSpeed",
            "signalPosition": "High",
            "cargoSpeed": "*",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("RS-314", "translate(5, 0)"),
            IconSvgGroup("RS-314", "translate(10, 0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS314Low",
        properties={
            "speedSignType": "MaximumSpeed",
            "signalPosition": "Low",
        },
        icon_groups=[
            IconSvgGroup("sign-lowered-base"),
            IconSvgGroup("RS-314", "translate(3, 0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS313",
        properties={
            "speedSignType": "DecelerateToSpeed",
            "signalPosition": "High",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("RS-313", "translate(6.5, 0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS313Bis",
        properties={
            "speedSignType": "DecelerateToSpeed",
            "signalPosition": "High",
            "cargoSpeed": "*",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("RS-313", "translate(4, 0)"),
            IconSvgGroup("RS-313", "translate(10, 0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS313Low",
        properties={
            "speedSignType": "DecelerateToSpeed",
            "signalPosition": "Low",
        },
        icon_groups=[
            IconSvgGroup("sign-lowered-base"),
            IconSvgGroup("RS-313", "translate(3, 0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS316",
        properties={
            "speedSignType": "AccelerateToSpeed",
            "signalPosition": "High",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("RS-316", "translate(6.5, 0)"),
        ],
    ),
    # todo
    # snelheid_ovw == LevelCrossingWeighBridgeSpeed == RS 324
    # goe_afrem
]

add_arrow_marker(signs)

signs.sort(key=lambda obj: obj.icon_name)
speed_sign_icon_entities_v124 = signs
