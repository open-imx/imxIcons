from pydantic import BaseModel


class IconRequestModel(BaseModel):
    """
    Model representing an icon request with a path and required properties.

    Attributes:
        imx_path: The file path to the IMX data for the icon.
        properties: A dictionary of required properties for the icon request.
        additional_properties: A dictionary of optional properties for the icon request, if any.
    """

    imx_path: str
    properties: dict[str, str | None]  # None is a valid imx value :L/
    additional_properties: dict[str, str] | None = None


class IconModel(BaseModel):
    """
    Model representing an icon with its metadata and optional properties.

    Attributes:
        imx_path: The file path to the IMX data for the icon.
        icon_name: The name of the icon.
        properties: A dictionary of required properties for the icon.
        additional_properties: A dictionary of optional properties for the icon, if any.
    """

    imx_path: str
    icon_name: str
    properties: dict[str, str]
    additional_properties: dict[str, str] | None = None
