from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "Sign"
imx_version = ImxVersionEnum.v124


def add_arrow_marker(sign):
    temp_list = []
    for item in sign:
        if any(
            substring in item.icon_name
            for substring in ["RS311", "RS249", "RS251aII", "RS331", "RS305"]
        ):
            continue
        translate = (
            "translate(-2.5, -1.15)"
            if "Low" in item.icon_name
            else "translate(-4, -1.15)"
        )
        temp_list.append(
            item.extend_icon(
                name=item.icon_name + "Arrow",
                extra_props={"hasArrowMarker": "True"},
                extra_groups=[IconSvgGroup("arrow-sign", f"rotate(180), {translate}")],
            )
        )
    sign.extend(temp_list)


RS300 = IconEntity(
    imx_version=imx_version,
    imx_path=entities_path,
    icon_name="RS300",
    properties={
        "signType": "StopSignCallOfficer",
    },
    icon_groups=[
        IconSvgGroup("sign-normal-base"),
        IconSvgGroup("sign-doghouse", "translate(6.5, 0)"),
        IconSvgGroup("RS-300", "translate(6.9, 0)"),
        IconSvgGroup("sign-doghouse-no-fill", "translate(6.5, 0)"),
        IconSvgGroup("RS-301", "translate(9.35, -.65), rotate(90)"),
        IconSvgGroup("sign-bottom-plate", "translate(4.75, 0)"),
    ],
)
RS301 = IconEntity(
    imx_version=imx_version,
    imx_path=entities_path,
    icon_name="RS301",  # can have witte lamp, then is 300cd
    properties={
        "signType": "StopSign",
    },
    icon_groups=[
        IconSvgGroup("sign-normal-base"),
        IconSvgGroup("sign-doghouse", "translate(6.5, 0)"),
        IconSvgGroup("RS-301", "translate(9.2, -.65), rotate(90)"),
        IconSvgGroup("sign-bottom-plate", "translate(4.75, 0)"),
    ],
)

RS301B = IconEntity(
    imx_version=imx_version,
    imx_path=entities_path,
    icon_name="RS301b",  # can have witte lamp, then is 300ef
    properties={
        "signType": "ProceedAfterPermission",
    },
    icon_groups=[
        IconSvgGroup("sign-normal-base"),
        IconSvgGroup("RS-301b", "translate(8, 0)"),
        IconSvgGroup("sign-bottom-plate", "translate(6.25, 0)"),
    ],
)

signs = [
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS375",
        properties={
            "signType": "CommandSign",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("sign-doghouse", "translate(6.5, 0)"),
            IconSvgGroup("RS-375", "translate(6.1, 0)"),
            IconSvgGroup("sign-bottom-plate", "translate(4.75, 0)"),
        ],
    ),
    RS300,
    RS300.extend_icon(
        "RS300ab",
        {"hasLamp": "True"},
        [
            IconSvgGroup("shunting-area-lamp", "translate(10, 0)"),
        ],
    ),
    RS301,
    RS301.extend_icon(
        "RS301cd",
        {"hasLamp": "True"},
        [
            IconSvgGroup("shunting-area-lamp", "translate(10, 0)"),
        ],
    ),
    RS301B,
    RS301B.extend_icon(
        "RS301ef",
        {"hasLamp": "True"},
        [
            IconSvgGroup("shunting-area-lamp", "translate(10, 0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS513",
        properties={
            "signType": "StopBeforeSignal",
        },
        icon_groups=[
            IconSvgGroup("sign-lowered-base"),
            IconSvgGroup("RS-513", "translate(4.2, 0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS243",
        properties={
            "signType": "LanternStop",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("sign-rectangle", "translate(6.5, 0)"),
            IconSvgGroup("RS-243", "translate(6.5, 0)"),
            IconSvgGroup("sign-rectangle-no-fill", "translate(6.5, 0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS244a",
        properties={
            "signType": "LanternSafe",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("sign-rectangle", "translate(6.5, 0)"),
            IconSvgGroup("RS-244a", "translate(6.5, 0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS306a",
        properties={
            "signType": "DisableTractionCurrent",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("sign-rectangle-45-degrees", "translate(8, 0)"),
            IconSvgGroup("RS-306a", "translate(8.1, 0.05), rotate(90), scale(0.8)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS307a",
        properties={
            "signType": "EnableTractionCurrent",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("sign-rectangle-45-degrees", "translate(8, 0)"),
            IconSvgGroup("RS-307a", "translate(8.1, 0.05), rotate(90), scale(0.8)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS311",
        properties={
            "signType": "EndOverheadLine",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("sign-rectangle-45-degrees", "translate(8, 0)"),
            IconSvgGroup("RS-311", "translate(8.1, 0.05), rotate(90), scale(0.8)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS311Left",
        properties={
            "signType": "EndOverheadLineLeft",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("RS-311-left", "translate(8, 0), scale(0.85)"),
            IconSvgGroup("sign-rectangle-45-degrees", "translate(8, 0)"),
            IconSvgGroup("RS-311", "translate(8.1, 0.05), rotate(90), scale(0.8)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS311Right",
        properties={
            "signType": "EndOverheadLineRight",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("RS-311-right", "translate(8, 0), rotate(180), scale(0.85)"),
            IconSvgGroup("sign-rectangle-45-degrees", "translate(8, 0)"),
            IconSvgGroup("RS-311", "translate(8.1, 0.05), rotate(90), scale(0.8)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="308a",
        properties={
            "signType": "EnableTractionCurrent",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("sign-rectangle-45-degrees", "translate(8, 0)"),
            IconSvgGroup("RS-308a", "translate(8, 0), scale(0.8)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS310a",
        properties={
            "signType": "RaisePantograph",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("sign-rectangle-45-degrees", "translate(8, 0)"),
            IconSvgGroup(
                "RS-RS309-RS-310a",
                "translate(8.1, 0.05), rotate(90), scale(0.8)",
            ),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS309a",
        properties={
            "signType": "PantographDown",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("sign-rectangle-45-degrees", "translate(8, 0)"),
            IconSvgGroup(
                "RS-RS309-RS-310a",
                "translate(8.1, 0.05), rotate(0), scale(0.8)",
            ),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS249",
        properties={
            "signType": "DistantSignalCountdownMarker",
        },
        icon_groups=[
            IconSvgGroup("RS-249", "translate(14, 0), rotate(180), scale(0.8)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS251aII",
        properties={
            "signType": "SignalCountdownMarker",
        },
        icon_groups=[
            IconSvgGroup("RS-251a-II", "translate(14, 0), rotate(180), scale(0.8)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS249a",
        properties={
            "signType": "ReduceSpeedCountdownMarker",
        },
        icon_groups=[
            IconSvgGroup("RS-249a", "translate(14, 0), rotate(180), scale(0.8)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS318a",
        properties={
            "signType": "LevelCrossingAnnouncement",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("RS-318", "translate(7, 0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS318b",
        properties={
            "signType": "DoubleLevelCrossingAnnouncement",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("RS-318", "translate(7, 0)"),
            IconSvgGroup("RS-318", "translate(12, 0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS331",
        properties={
            "signType": "Block",
        },
        icon_groups=[
            IconSvgGroup("RS-331"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS305",
        properties={
            "signType": "HaltAhead",
        },
        icon_groups=[
            IconSvgGroup("RS-305"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS304a",
        properties={
            "signType": "TrainLength",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("sign-rectangle-45-degrees", "translate(8, 0)"),
            IconSvgGroup("RS-304a", "translate(8, 0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS304b",
        properties={
            "signType": "TrainLengthSingle",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("sign-rectangle-45-degrees", "translate(8, 0)"),
            IconSvgGroup("RS-304a", "translate(8, 0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS304c",
        properties={
            "signType": "TrainLengthDouble",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("sign-rectangle-45-degrees", "translate(8, 0)"),
            IconSvgGroup("RS-304c", "translate(8, 0), rotate(-90)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="TextSign",
        properties={
            "signType": "TextSign",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("sign-bottom-plate", "translate(7, 0), scale(1.2)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS336",
        properties={
            "signType": "EnableEtcsCabSignalling",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("RS-336", "translate(8,0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS337",
        properties={
            "signType": "DisableEtcsCabSignalling",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("RS-336", "translate(8,0)"),
            IconSvgGroup("RS-337", "translate(8,0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS226a",
        properties={
            "signType": "DecelerateLevelCrossing",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("RS-313", "translate(6, 0)"),
            IconSvgGroup("RS-226a-under-sign", "translate(4.5, 0)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS253a",
        properties={
            "signType": "SwitchLeft",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("RS-253", "translate(10.1, -1.5), rotate(90), scale(0.8)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS253b",
        properties={
            "signType": "SwitchRight",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("RS-253", "translate(7.1, 1.5), rotate(-90), scale(0.8)"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="RS333",
        properties={
            "signType": "EndTrainVacancyDetection",
        },
        icon_groups=[
            IconSvgGroup("sign-normal-base"),
            IconSvgGroup("sign-rectangle-45-degrees", "translate(8, 0)"),
            IconSvgGroup("RS-333", "translate(8.05, 0.05), rotate(90)"),
        ],
    ),
]

add_arrow_marker(signs)

signs.sort(key=lambda obj: obj.icon_name)
sign_icon_entities_v124 = signs
