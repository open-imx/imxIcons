from enum import Enum
from typing import Literal

icon_types_literal = Literal["svg", "svg_dark", "qgis", "qgis_dark"]


class IconTypesEnum(Enum):
    """Enum representing different types of icons."""

    svg = "svg"
    """Represents Scalable Vector Graphics."""

    svg_dark = "svg_dark"
    """Represents Scalable Vector Graphics in dark theme."""

    qgis = "qgis"
    """Represents Scalable Vector Graphics whit QGIS parameters."""

    qgis_dark = "qgis_dark"
    """Represents Scalable Vector Graphics whit QGIS parameters in dark theme."""

    @classmethod
    def from_string(cls, value: str):
        try:
            return IconTypesEnum[value]
        except KeyError:  # pragma: no cover
            raise ValueError(f"should be a valid icon type: {icon_types_literal}")  # NOQA  TRY003
