from enum import Enum


class ImxVersionEnum(Enum):
    """
    Enumeration representing different versions of the IMX format.

    Members:
        v124: Represents version 1.2.4 of the IMX format.
        v500: Represents version 5.0.0 of the IMX format.
    """

    v124 = "IMX-v1.2.4"
    v500 = "IMX-v5.0.0"
