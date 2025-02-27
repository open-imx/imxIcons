from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "DepartureSignal"
imx_version = ImxVersionEnum.v500


departure_signal_entities_imx500 = [
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="DepartureSingle",
        properties={"departureSignalType": "DepartureSingle"},
        icon_groups=[
            IconSvgGroup("departure-single", "rotate(180)"),
            IconSvgGroup("departure"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="DepartureDouble",
        properties={"departureSignalType": "DepartureDouble"},
        icon_groups=[
            IconSvgGroup("departure-double", "rotate(180)"),
            IconSvgGroup("departure"),
        ],
    ),
]
