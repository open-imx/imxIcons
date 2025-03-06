import asyncio
import shutil
from pathlib import Path

from imxIcons.iconService import IconService
from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.domain.icon_library import ICON_DICT
from imxIcons.iconServiceModels import IconRequestModel


async def create_asset_folder(base_dir: Path = Path(__file__).parent):
    base_path = Path(base_dir / "icon_renders")

    if base_path.exists() and base_path.is_dir():
        shutil.rmtree(base_path)

    base_path.mkdir(parents=True, exist_ok=True)

    folder_dict = {}
    for folder in [_.name for _ in ImxVersionEnum]:
        imx_version_folder = base_path / folder
        imx_version_folder.mkdir(parents=True, exist_ok=True)
        folder_dict[folder] = imx_version_folder

    for imx_path, versions in ICON_DICT.items():
        for version, icons in versions.items():
            icon_folder_base = folder_dict[version]

            for icon in icons:
                svg_content = IconService.get_svg(
                    IconRequestModel(
                        imx_path=icon.imx_path, properties=icon.properties, additional_properties=icon.additional_properties
                    ),
                    ImxVersionEnum[version],
                    icon_type="svg_dark"
                )
                file_path = icon_folder_base / f"{icon.icon_name}.svg"
                file_path.write_text(svg_content, encoding="utf-8")


if __name__ == "__main__":
    asyncio.run(create_asset_folder())
