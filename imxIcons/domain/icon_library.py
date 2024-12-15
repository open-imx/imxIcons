from imxIcons.domain.atbvvInstallation.atbvvBeacon_v124 import (
    atbvv_beacon_entities_v124,
)
from imxIcons.domain.atbvvInstallation.atbvvBeacon_v500 import (
    atbvv_beacon_entities_v500,
)
from imxIcons.domain.axleCounterDetection.axleCounterDetectionPoint_v124 import (
    axle_counter_points_icon_entities_v124,
)
from imxIcons.domain.axleCounterDetection.axleCounterDetectionPoint_v500 import (
    axle_counter_points_icon_entities_v500,
)
from imxIcons.domain.departureSignal.departureSignal_imx500 import (
    departure_signal_entities_imx500,
)
from imxIcons.domain.insulatedJoint.insulatedJoint_v124 import (
    insulated_joint_entities_v124,
)
from imxIcons.domain.insulatedJoint.insulatedJoint_v500 import (
    insulated_joint_entities_v500,
)
from imxIcons.domain.levelCrossing.levelCrossing_v124 import (
    level_crossing_entities_v124,
)
from imxIcons.domain.levelCrossing.levelCrossing_v500 import (
    level_crossing_entities_v500,
)
from imxIcons.domain.sign.sign_imx124 import sign_icon_entities_v124
from imxIcons.domain.sign.sign_imx500 import sign_icon_entities_v500
from imxIcons.domain.signal.illuminated_signal_v124 import (
    illuminated_sign_icon_entities_v124,
)
from imxIcons.domain.signal.illuminated_signal_v500 import (
    illuminated_sign_icon_entities_v500,
)
from imxIcons.domain.signal.reflector_signal_v124 import (
    reflector_post_icon_entities_v124,
)
from imxIcons.domain.signal.reflector_signal_v500 import (
    reflector_post_icon_entities_v500,
)
from imxIcons.domain.signal.signal_imx124 import signals_icon_entities_v124
from imxIcons.domain.signal.signal_imx500 import signals_icon_entities_v500
from imxIcons.domain.speedsign.speedsign_imx124 import speed_sign_icon_entities_v124
from imxIcons.domain.speedsign.speedsign_imx500 import speed_sign_icon_entities_v500
from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity


def validate_icon_set(icons: list[IconEntity]) -> list[IconEntity]:
    """
    Validates a list of IconEntity objects for duplicates and consistency.

    Checks for:
    - Duplicate properties among the icons.
    - Duplicate icon names.
    - Consistent `imx_path` across all icons.

    Args:
        icons: A list of IconEntity objects to validate.

    Returns:
        The validated list of IconEntity objects.

    Raises:
        ValueError: If any duplicate properties, duplicate icon names,
                    or inconsistent `imx_path` are found.
    """

    property_map: dict[tuple, IconEntity] = {}
    icon_name_map: dict[str, IconEntity] = {}
    imx_path = icons[0].imx_path

    for icon in icons:
        if icon.imx_path != imx_path:
            raise ValueError(
                f"Inconsistent imx_path found: {icon.icon_name} has path {icon.imx_path}, expected {imx_path}"
            )

        property_tuple = tuple(sorted(icon.properties.items()))
        if property_tuple in property_map:
            raise ValueError(
                f"Duplicate properties found for icon: {icon.icon_name} and {property_map[property_tuple].icon_name}"
            )
        else:
            property_map[property_tuple] = icon

        if icon.icon_name in icon_name_map:
            raise ValueError(f"Duplicate icon name found: {icon.icon_name}")
        else:
            icon_name_map[icon.icon_name] = icon

    return icons


ICON_DICT: dict[str, dict[str, list[IconEntity]]] = {
    "DepartureSignal": {
        ImxVersionEnum.v124.name: [],  # DepartureSignal is a SignalType in v124
        ImxVersionEnum.v500.name: validate_icon_set(departure_signal_entities_imx500),
    },
    "Signal": {
        ImxVersionEnum.v124.name: validate_icon_set(signals_icon_entities_v124),
        ImxVersionEnum.v500.name: validate_icon_set(signals_icon_entities_v500),
    },
    "Signal.IlluminatedSign": {
        ImxVersionEnum.v124.name: validate_icon_set(
            illuminated_sign_icon_entities_v124
        ),
        ImxVersionEnum.v500.name: validate_icon_set(
            illuminated_sign_icon_entities_v500
        ),
    },
    "Signal.ReflectorPost": {
        ImxVersionEnum.v124.name: validate_icon_set(reflector_post_icon_entities_v124),
        ImxVersionEnum.v500.name: validate_icon_set(reflector_post_icon_entities_v500),
    },
    "SpeedSign": {
        ImxVersionEnum.v124.name: validate_icon_set(speed_sign_icon_entities_v124),
        ImxVersionEnum.v500.name: validate_icon_set(speed_sign_icon_entities_v500),
    },
    "Sign": {
        ImxVersionEnum.v124.name: validate_icon_set(sign_icon_entities_v124),
        ImxVersionEnum.v500.name: validate_icon_set(sign_icon_entities_v500),
    },
    "AxleCounterDetectionPoint": {
        ImxVersionEnum.v124.name: validate_icon_set(
            axle_counter_points_icon_entities_v124
        ),
        ImxVersionEnum.v500.name: validate_icon_set(
            axle_counter_points_icon_entities_v500
        ),
    },
    "LevelCrossing": {
        ImxVersionEnum.v124.name: validate_icon_set(level_crossing_entities_v124),
        ImxVersionEnum.v500.name: validate_icon_set(level_crossing_entities_v500),
    },
    "ATBVVInstallation.ATBVVBeacon": {
        ImxVersionEnum.v124.name: validate_icon_set(atbvv_beacon_entities_v124),
        ImxVersionEnum.v500.name: [],
    },
    "AtbVvInstallation.AtbVvBeacon": {
        ImxVersionEnum.v124.name: [],
        ImxVersionEnum.v500.name: validate_icon_set(atbvv_beacon_entities_v500),
    },
    "InsulatedJoint": {
        ImxVersionEnum.v124.name: validate_icon_set(insulated_joint_entities_v124),
        ImxVersionEnum.v500.name: validate_icon_set(insulated_joint_entities_v500),
    },
}


DEFAULT_ICONS: dict[str, IconEntity | None] = {
    "Signal": None,
    "Signal.IlluminatedSign": None,
    "Signal.ReflectorPost": None,
    "SpeedSign": None,
    "Sign": None,
}
