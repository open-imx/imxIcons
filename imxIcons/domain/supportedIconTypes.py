from enum import Enum
from typing import Literal

icon_types_literal = Literal["svg", "qgis"]


class IconTypesEnum(Enum):
    svg = "svg"
    qgis = "qgis"

    @classmethod
    def from_string(cls, value: str):
        try:
            return IconTypesEnum[value]
        except KeyError:  # pragma: no cover
            raise ValueError(f"should be a valid icon type: {icon_types_literal}")  # NOQA  TRY003
