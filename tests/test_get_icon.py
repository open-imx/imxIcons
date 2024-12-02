from imxIcons.domain.svg_data import qgis_render

from imxIcons.domain import ImxVersionEnum
from imxIcons.iconService import IconService
from imxIcons.iconServiceModels import IconRequestModel

def test_v124():
    svg = IconService.get_svg(
        IconRequestModel(
            imx_path="Signal",
            properties={
                "signalType": "AutomaticPermissive",
                "signalPosition": "High",
                "isMountedOnGantry": "True",
                "hasArrowMarker": "True"
        }),
        ImxVersionEnum.v124
    )
    assert "AutomaticPermissiveGantryArrow" in svg, "returned type not correct"

def test_non_pretty_svg():
    svg = IconService.get_svg(
        IconRequestModel(
            imx_path="Signal",
            properties={
                "signalType": "AutomaticPermissive",
                "signalPosition": "High",
                "isMountedOnGantry": "True",
                "hasArrowMarker": "True"
        }),
        ImxVersionEnum.v124,
        pretty_svg=False,
    )
    assert '\n' in svg, "should not have newlines"


def test_v500():
    svg = IconService.get_svg(
        IconRequestModel(
            imx_path="Signal",
            properties={
                "signalType": "AutomaticPermissive",
                "signalPosition": "High",
                "gantryRef": "*",
                "hasArrowMarker": "True"
        }),
        ImxVersionEnum.v500
    )
    assert "AutomaticPermissiveGantryArrow" in svg, "returned type not correct"


def test_get_icon_name_v124():
    name = IconService.get_icon_name(
        IconRequestModel(
            imx_path="Signal",
            properties={
                "signalType": "AutomaticPermissive",
                "signalPosition": "High",
                "isMountedOnGantry": "True",
                "hasArrowMarker": "True"
            }),
        ImxVersionEnum.v124
    )
    assert name == 'AutomaticPermissiveGantryArrow'


def test_get_icon_name_v500():
    name = IconService.get_icon_name(
        IconRequestModel(
            imx_path="Signal",
            properties={
                "signalType": "AutomaticPermissive",
                "signalPosition": "High",
                "gantryRef": "*",
                "hasArrowMarker": "True"
            }),
        ImxVersionEnum.v500
    )
    assert name == 'AutomaticPermissiveGantryArrow'


def test_get_all_icons_v124():
    icon_dict = IconService.get_all_icons(ImxVersionEnum.v124)
    assert len(icon_dict.keys()) == 442
    signal_high = icon_dict.get('SignalHigh')
    assert all(key in signal_high for key in [
        'imx_version', 'imx_path', 'imx_properties', 'icon'
    ]), "Not all keys are in the dictionary"

