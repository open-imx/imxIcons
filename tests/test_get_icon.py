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
