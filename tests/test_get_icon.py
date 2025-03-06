from imxIcons.domain.supportedImxVersions import ImxVersionEnum
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


def test_get_icon_additional_properties():
    name = IconService.get_icon_name(
        IconRequestModel(
            imx_path="Sign",
            properties={
                "signType": "LevelCrossingAnnouncement",
                "hasArrowMarker": "True"
            },
            additional_properties={"ArrowMarkerDouble": "True"}
        ),
        ImxVersionEnum.v124
    )
    assert name == 'RS318aArrowDouble'


def test_get_all_icons_v124():
    icon_dict = IconService.get_all_icons(ImxVersionEnum.v124)
    assert len(icon_dict.keys()) == 545
    signal_high = icon_dict.get('SignalHigh')
    assert '"param(' not in signal_high['icon'], 'Should not have "param(" in icon string'
    assert all(key in signal_high for key in [
        'imx_version', 'imx_path', 'imx_properties', 'icon'
    ]), "Not all keys are in the dictionary"


def test_get_all_icons_v124_qgis():
    icon_dict = IconService.get_all_icons(ImxVersionEnum.v124, icon_type="qgis")
    assert len(icon_dict.keys()) == 545
    signal_high = icon_dict.get('SignalHigh')
    assert '"param(' in signal_high['icon'], 'Should have "param(" in icon string'
    assert all(key in signal_high for key in [
        'imx_version', 'imx_path', 'imx_properties', 'icon'
    ]), "Not all keys are in the dictionary"

