from pydantic import BaseModel


class IconRequestModel(BaseModel):
    imx_path: str
    properties: dict[str, str]
    optional_properties: dict[str, str] | None = None


class IconModel(BaseModel):
    imx_path: str
    icon_name: str
    properties: dict[str, str]
    optional_properties: dict[str, str] | None = None
