
# Assembly of Icons

To implement an icon in the `icon_library.py`, follow these steps:

1. Break the icon into reusable parts.
2. Assemble the icon for each IMX version.
3. Add a unique mapping to the icon.
4. Include the assembly in the icon library.

For clarity, we will look at the Signal icon. However, an insulatedJoint example may be simpler to understand.

---

## 1. Create SVG Snippets

After designing an icon (or a set of icons), break it into modular parts. This ensures SVG snippets can be reused across different icons for consistency and efficiency.

Each part is stored as an SVG group (`<g>...</g>`) in the `svg_data.py` file, located in the `imxIcons/domain` folder.

- The `get_svg_groups()` method holds these groups, enabling adjustments for QGIS icons and other potential SVG subtypes.
- Use `get_svg_groups()` to create a dictionary of SVG snippets for each icon type. The group name acts as the key to access its corresponding snippet.

### Example: Reusable SVG Snippets

The following example illustrates creating four symbols with three stamps. This approach minimizes boilerplate while maintaining flexibility and consistency.

```html
<!-- Unknown rail icon -->
<g name="insulatedJoint" {create_primary_icon_style(qgis_render)}>
    <line y1="1.5" y2="-1.5" />
</g>

<!-- Add this if left (or both) -->
<g name="insulatedJoint-left" {create_primary_icon_style(qgis_render)}>
  <line x1="-.75" y1="-1.5" x2=".75" y2="-1.5" style="stroke: rgb(0, 0, 0); stroke-width: 0.25px;" />
</g>

<!-- Add this if rail is right (or both) --> 
<g name="insulatedJoint-right" {create_primary_icon_style(qgis_render)}>
  <line x1="-.75" y1="1.5" x2=".75" y2="1.5" style="stroke: rgb(0, 0, 0); stroke-width: 0.25px;" />
</g>
```

> **Note:** We have two identical lines that could be transposed instead of duplicated. However, this would reduce intuitiveness and increase complexity.

---

## 2. File Structure

In the domain folder, icons are organized into subfolders grouped by parent-child relationships or system-related clusters. Each supported IMX version has its own file for the icons. Icons not present in a version should not have a corresponding file.

### Example File Structure

```bash
imxIcons/domain/signal
├── __init__.py
├── illuminated_signal_v124.py       # v124 illuminated signal
├── illuminated_signal_v500.py       # v500 illuminated signal
├── signal_imx124.py                 # IMX v124 signals (with departure signals)
└── signal_imx500.py                 # IMX v500 signals (without departure signals)

imxIcons/domain/departureSignal
├── __init__.py
└── departureSignal_imx500.py        # v500 departure signals

imxIcons/
├── svg_data.py                      # SVG snippets
└── icon_library.py                  # ICON_DICT for all icons
```

---

## 3. Assemble Icons

In the domain files, assemble icons by defining their properties and groups.

### Example Icon Definition

```python
from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "DepartureSignal"
imx_version = ImxVersionEnum.v500

departure_signal_entities_imx500 = [
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="DepartureSingle",
        properties={"departureSignalType": "DepartureSingle"},
        icon_groups=[
            IconSvgGroup("departure-single"),
            IconSvgGroup("departure"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="DepartureDouble",
        properties={"departureSignalType": "DepartureDouble"},
        icon_groups=[
            IconSvgGroup("departure-double"),
            IconSvgGroup("departure"),
        ],
    ),
]
```

---

## 4. Handle Complex Icons

For icons with many variations, use methods to stamp SVG snippets onto existing icons. 

### Example: Adding Danger Signs

```python
from imxIcons.iconEntity import IconEntity, IconSvgGroup

def add_danger_sign(signals: list[IconEntity]):
    for item in signals:
        if item.icon_name in ["SignalHigh", "SignalGantry", "AutomaticPermissiveHigh"]:
            signals.append(
                item.extend_icon(
                    name=f"{item.icon_name}Danger",
                    extra_props={"hasDangerSign": "True"},
                    extra_groups=[
                        IconSvgGroup("signal-danger-sign", "translate(4.25, 0)")
                    ],
                )
            )

signals = [...]  # Predefined icons
add_danger_sign(signals)
```

---

## 5. Add Icons to the Icon Library

After creating icons, include them in `icon_library.py` by importing and adding them to `ICON_DICT`. The dictionary key is the IMX path.

### Example: Updating the Library

```python
from imxIcons.domain.signal.signal_imx124 import signals_icon_entities_v124
from imxIcons.domain.signal.signal_imx500 import signals_icon_entities_v500
from imxIcons.domain.departureSignal.departureSignal_imx500 import departure_signal_entities_imx500

ICON_DICT: dict[str, dict[str, list[IconEntity]]] = {
    "DepartureSignal": {
        ImxVersionEnum.v124.name: [],  # No DepartureSignal in v124
        ImxVersionEnum.v500.name: departure_signal_entities_imx500,
    },
    "Signal": {
        ImxVersionEnum.v124.name: signals_icon_entities_v124,
        ImxVersionEnum.v500.name: signals_icon_entities_v500,
    },
}
```

---

## 6. Test Icons

1. Run `hatch run test` in the terminal to ensure 100% coverage.
2. Verify the generated documentation includes the created icons.
3. Optionally, run `create_all_icons.py` to generate SVG files in the root `icon_renders` folder.
