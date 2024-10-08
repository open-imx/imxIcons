from pydantic import BaseModel


class IconRequestModel(BaseModel):
    """Model representing an icon request with a path and required properties."""
    imx_path: str
    properties: dict[str, str]
    optional_properties: dict[str, str] | None = None


class IconModel(BaseModel):
    """Model representing an icon with its metadata and optional properties."""
    imx_path: str
    icon_name: str
    properties: dict[str, str]
    optional_properties: dict[str, str] | None = None
