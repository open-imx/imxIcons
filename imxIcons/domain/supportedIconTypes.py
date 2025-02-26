from enum import Enum
from typing import Literal

icon_types_literal = Literal["svg", "qgis"]


class IconTypesEnum(Enum):
    """Enum representing different types of icons."""

    svg = "svg"
    """Represents Scalable Vector Graphics."""

    qgis = "qgis"
    """Represents Scalable Vector Graphics whit QGIS parameters."""

    @classmethod
    def from_string(cls, value: str):
        try:
            return IconTypesEnum[value]
        except KeyError:  # pragma: no cover
            raise ValueError(f"should be a valid icon type: {icon_types_literal}")  # NOQA  TRY003
