from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "Signal"
imx_version = ImxVersionEnum.v500


signals = []


# Extension functions
def add_shunting(signals):
    temp_list = []
    for item in signals:
        # can be applied to normal high and low signals
        if item.icon_name in ["SignalLow", "SignalHigh"]:
            translate = (
                "translate(5.25, 0)"
                if "SignalLow" in item.icon_name
                else "translate(11.5, 0)"
            )
            temp_list.append(
                item.extend_icon(
                    name=item.icon_name + "Shunting",
                    extra_props={"hasShuntingIndicator": "True"},
                    extra_groups=[IconSvgGroup("shunting-area-lamp", translate)],
                )
            )
    signals.extend(temp_list)


def add_danger_sign(signals):
    temp_list = []
    for item in signals:
        if item.icon_name in [
            "SignalHigh",
            "SignalGantry",
            "AutomaticPermissiveHigh",
            "AutomaticPermissiveGantry",
            "SignalHighShunting",
        ]:
            temp_list.append(
                item.extend_icon(
                    name=item.icon_name + "Danger",
                    extra_props={"hasDangerSign": "True"},
                    extra_groups=[
                        IconSvgGroup("signal-danger-sign", "translate(4.25, 0)")
                    ],
                )
            )
    signals.extend(temp_list)


def add_spreader_lens(signals):
    temp_list = []
    for item in signals:
        if any(
            group.group_id in ["signal-aspect", "signal-distance"]
            for group in item.icon_groups
        ):
            translate = (
                "translate(1.75, 0)" if "Low" in item.icon_name else "translate(8, 0)"
            )
            temp_list.append(
                item.extend_icon(
                    name=item.icon_name + "Lens",
                    extra_props={"hasSpreaderLens": "True"},
                    extra_groups=[IconSvgGroup("signal-spreader-lens", translate)],
                )
            )
    signals.extend(temp_list)


def add_white_bar(signals):
    temp_list = []
    for item in signals:
        if (
            "Distance" in item.icon_name
            or "AutomaticPermissive" in item.icon_name
            or "Low" in item.icon_name
        ):
            continue
        if any(
            group.group_id in ["signal-aspect", "signal-distance"]
            for group in item.icon_groups
        ):
            if any(
                group.group_id == "signal-spreader-lens" for group in item.icon_groups
            ):
                transpose = "translate(8, -2.75)"
            else:
                transpose = "translate(8, -2.25)"

            temp_list.append(
                item.extend_icon(
                    name=item.icon_name + "Whitebar",
                    extra_props={"hasWhitebarETCSIndicator": "True"},
                    extra_groups=[IconSvgGroup("signal-white-bar", transpose)],
                )
            )
    signals.extend(temp_list)


def add_arrow_marker(signals):
    temp_list = []
    for item in signals:
        if any(
            group.group_id
            in [
                "repeat",
                "signal-cargo",
                "signal-distant-cargo",
                "signal-aspect",
                "signal-distance",
            ]
            for group in item.icon_groups
        ):
            translate = (
                "translate(-2, -1.15)"
                if "SignalLow" in item.icon_name
                else "translate(-2.5, -1.15)"
            )
            temp_list.append(
                item.extend_icon(
                    name=item.icon_name + "Arrow",
                    extra_props={"hasArrowMarker": "True"},
                    extra_groups=[
                        IconSvgGroup("arrow-sign", f"rotate(180), {translate}")
                    ],
                )
            )
    signals.extend(temp_list)


def add_out_of_service(signals):
    # todo: define the types that can be taken out of service, also merge initialing so we run all methods on one place
    temp_list = []
    for item in signals:
        translate = (
            "translate(3.75, 0)"
            if "SignalLow" in item.icon_name
            else "translate(10, 0)"
        )
        temp_list.append(
            item.extend_icon(
                name=item.icon_name + "NoService",
                extra_props={"isOutOfService": "True"},
                extra_groups=[IconSvgGroup("signal-out-of-service", translate)],
            )
        )
    signals.extend(temp_list)


def add_cow_heads(signals):
    temp_list = []
    for item in signals:
        if (
            "Distance" in item.icon_name
            or "AutomaticPermissive" in item.icon_name
            or "Low" in item.icon_name
        ):
            continue

        temp_list.append(
            item.extend_icon(
                name=item.icon_name + "CowHead",
                extra_props={"hasDirectionIndicator": "2"},
                extra_groups=[
                    IconSvgGroup("signal-direction-sign", "translate(1.5, 0)")
                ],
            )
        )
        temp_list.append(
            item.extend_icon(
                name=item.icon_name + "CowHeadThreeWay",
                extra_props={"hasDirectionIndicator": "3"},
                extra_groups=[
                    IconSvgGroup("signal-direction-3-sign", "translate(1.5, 0)")
                ],
            )
        )

    signals.extend(temp_list)


# Base signals creation
signals.extend(
    [
        IconEntity(
            imx_version=imx_version,
            imx_path=entities_path,
            icon_name="SignalLow",
            properties={"signalType": "Controlled", "signalPosition": "Low"},
            icon_groups=[
                IconSvgGroup("post-ground"),
                IconSvgGroup("signal-post-low"),
                IconSvgGroup("signal-aspect", "translate(3.75, 0)"),
            ],
        ),
        IconEntity(
            imx_version=imx_version,
            imx_path=entities_path,
            icon_name="SignalHigh",
            properties={"signalType": "Controlled", "signalPosition": "High"},
            icon_groups=[
                IconSvgGroup("post-ground"),
                IconSvgGroup("signal-post-high"),
                IconSvgGroup("signal-aspect", "translate(10, 0)"),
                IconSvgGroup("illuminated-sign-integrated", "translate(7.25, 0)"),
            ],
        ),
        IconEntity(
            imx_version=imx_version,
            imx_path=entities_path,
            icon_name="SignalGantry",
            properties={
                "signalType": "Controlled",
                "signalPosition": "High",
                "gantryRef": "*",
            },
            icon_groups=[
                IconSvgGroup("signal-post-high"),
                IconSvgGroup("signal-aspect", "translate(10, 0)"),
            ],
        ),
        IconEntity(
            imx_version=imx_version,
            imx_path=entities_path,
            icon_name="AutomaticPermissiveHigh",
            properties={"signalType": "AutomaticPermissive", "signalPosition": "High"},
            icon_groups=[
                IconSvgGroup("post-ground"),
                IconSvgGroup("signal-post-high"),
                IconSvgGroup("signal-aspect", "translate(10, 0)"),
                IconSvgGroup("signal-p", "translate(1, 3.5), rotate(90)"),
            ],
        ),
        IconEntity(
            imx_version=imx_version,
            imx_path=entities_path,
            icon_name="AutomaticPermissiveGantry",
            properties={
                "signalType": "AutomaticPermissive",
                "signalPosition": "High",
                "gantryRef": "*",
            },
            icon_groups=[
                IconSvgGroup("signal-post-high"),
                IconSvgGroup("signal-aspect", "translate(10, 0)"),
                IconSvgGroup("signal-p", "translate(1, 3.5), rotate(90)"),
            ],
        ),
        IconEntity(
            imx_version=imx_version,
            imx_path=entities_path,
            icon_name="Distance",
            properties={"signalType": "Distance"},
            icon_groups=[
                IconSvgGroup("post-ground"),
                IconSvgGroup("signal-post-high"),
                IconSvgGroup("signal-distance"),
            ],
        ),
        IconEntity(
            imx_version=imx_version,
            imx_path=entities_path,
            icon_name="DistanceGantry",
            properties={"signalType": "Distance", "gantryRef": "*"},
            icon_groups=[
                IconSvgGroup("signal-post-high"),
                IconSvgGroup("signal-distance"),
            ],
        ),
    ]
)


# Applying extensions
add_shunting(signals)
add_danger_sign(signals)
add_spreader_lens(signals)
add_cow_heads(signals)
add_white_bar(signals)
add_out_of_service(signals)


signals.extend(
    [
        IconEntity(
            imx_version=imx_version,
            imx_path=entities_path,
            icon_name="Repeat",
            properties={"signalType": "Repeat"},
            icon_groups=[
                IconSvgGroup("post-ground"),
                IconSvgGroup("signal-post-high"),
                IconSvgGroup("repeat"),
            ],
        ),
        IconEntity(
            imx_version=imx_version,
            imx_path=entities_path,
            icon_name="RepeatGantry",
            properties={"signalType": "Repeat", "gantryRef": "*"},
            icon_groups=[
                IconSvgGroup("signal-post-high"),
                IconSvgGroup("repeat"),
            ],
        ),
        IconEntity(
            imx_version=imx_version,
            imx_path=entities_path,
            icon_name="CargoSignal",
            properties={"signalType": "CargoSignal"},
            icon_groups=[
                IconSvgGroup("post-ground"),
                IconSvgGroup("signal-post-high"),
                IconSvgGroup("signal-cargo"),
            ],
        ),
        IconEntity(
            imx_version=imx_version,
            imx_path=entities_path,
            icon_name="CargoSignalGantry",
            properties={"signalType": "CargoSignal", "gantryRef": "*"},
            icon_groups=[
                IconSvgGroup("signal-post-high"),
                IconSvgGroup("signal-cargo"),
            ],
        ),
        IconEntity(
            imx_version=imx_version,
            imx_path=entities_path,
            icon_name="CargoSignalDistant",
            properties={"signalType": "DistantCargoSignal"},
            icon_groups=[
                IconSvgGroup("post-ground"),
                IconSvgGroup("signal-post-high"),
                IconSvgGroup("signal-distant-cargo"),
            ],
        ),
        IconEntity(
            imx_version=imx_version,
            imx_path=entities_path,
            icon_name="CargoSignalDistantGantry",
            properties={"signalType": "DistantCargoSignal", "gantryRef": "*"},
            icon_groups=[
                IconSvgGroup("signal-post-high"),
                IconSvgGroup("signal-distant-cargo"),
            ],
        ),
    ]
)
# Additional signals creation

add_arrow_marker(signals)

signals.append(
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="0_KerstBoom",
        properties={"*": "*"},
        icon_groups=[
            IconSvgGroup("post-ground"),
            IconSvgGroup("post-ground"),
            IconSvgGroup("signal-post-high"),
            IconSvgGroup("signal-aspect", "translate(10, 0)"),
            IconSvgGroup("signal-p", "translate(1, 3.5), rotate(90)"),
            IconSvgGroup("illuminated-sign-integrated", "translate(7.25, 0)"),
            IconSvgGroup("signal-danger-sign", "translate(4.25, 0)"),
            IconSvgGroup("signal-direction-3-sign", "translate(1.5, 0)"),
            IconSvgGroup("signal-white-bar", "translate(8, -2.75)"),
            IconSvgGroup("signal-spreader-lens", "translate(8, 0)"),
            IconSvgGroup("shunting-area-lamp", "translate(11.5, 0)"),
            IconSvgGroup("arrow-sign", "rotate(180), translate(-2.5, -1.15)"),
            IconSvgGroup("signal-out-of-service", "translate(10, 0)"),
        ],
    )
)


# Final sorting and assignment
signals.sort(key=lambda obj: obj.icon_name)
signals_icon_entities_v500 = signals
