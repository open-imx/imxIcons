
# Assembly of Icons

Now that you have a great set of icons, you might want to include them in the library. 
The easiest way to do this is to simply send them over, and we’ll take care of the implementation for you. 
Or just be a bad ass and implement them yourself 😎.

To implement an icon follow these steps:

1. Break the icon into reusable parts.
2. Create files for every IMX version we support. 
3. Assemble the icon for each IMX version.
4. Include the assembly in the icon library.

---

## File Structure
In the domain folder, the file `svg_data.py` holds the SVG data, the `icon_library,py` contains functionality to the access the icons.

In the domain folder, icons definition files are organized into subfolders grouped by parent-child relationships or system-related clusters. 
Each supported IMX version has its own file for the icons. Icons not present in a version should not have a corresponding file.

For example, in IMX version 1.2.4. a `DepartureSignal` is defined as a signal type within an attribute of a IMX `Signal`. 
In IMX 5.0.0 it is defined as a dedicated IMX object. 
This results in the following file structure, with comments highlighting key points of interest.

```bash
imxIcons/domain/departureSignal
├── __init__.py
└── departureSignal_imx500.py        # v500 departure signals

imxIcons/domain/signal
├── __init__.py
├── illuminated_signal_v124.py       # v124 illuminated signal
├── illuminated_signal_v500.py       # v500 illuminated signal
├── signal_imx124.py                 # v124 signals (with departure signals)
└── signal_imx500.py                 # v500 signals (without departure signals)

imxIcons/domain
├── svg_data.py                      # SVG snippets
└── icon_library.py                  # ICON_DICT for all icons
```

---

## Create SVG Snippets

After designing an icon (or a set of icons), break it into modular parts. This ensures SVG snippets can be reused across different icons for consistency and efficiency.
Each part is stored as an SVG group in the `svg_data.py`,

- The `get_svg_groups()` method holds these SVG groups and sets the primary style by interpolation. This way we support normal, QGIS icons and maybe in the future other potential SVG subtypes.
- We use `get_svg_groups()` to create a dictionary for each icon type (`SVG_SVG_GROUP_DICT` and `QGIS_SVG_GROUP_DICT`). The group name acts as the key to access its corresponding SVG snippet.


Below is a simple example of breaking an icon into reusable parts as SVG snippets. The icon is divided into three parts.
While this might seem like a lot of boilerplate, this approach is incredibly useful for handling complex cases and ensuring consistency across icons.

```html
<!-- Unknown rail icon -->
<g name="insulatedJoint" {create_primary_icon_style(qgis_render)}>
    <line y1="1.5" y2="-1.5" />
</g>

<!-- Add this if rail is left (or both) -->
<g name="insulatedJoint-left" {create_primary_icon_style(qgis_render)}>
  <line x1="-.75" y1="-1.5" x2=".75" y2="-1.5" style="stroke-width: 0.25px;" />
</g>

<!-- Add this if rail is right (or both) --> 
<g name="insulatedJoint-right" {create_primary_icon_style(qgis_render)}>
  <line x1="-.75" y1="1.5" x2=".75" y2="1.5" style="stroke-width: 0.25px;" />
</g>
```

> **Note:** We have two identical lines that could be transposed instead of duplicated. However, this would reduce intuitiveness and increase complexity.

---

## Assemble Icons

To correctly reference icons we use the IMX path.
The IMX path contains multiple XML tags to represent parent-child relationships up to the first object containing a puic attribute. 

> **For example:** `SingleSwitch.SwitchMechanism.Lock` may refer to one icon, while another icon could be associated with `Bridge.Lock`. 


In the domain files, icons are assembled by defining a icon name, property mapping and (set of) SVG snippets. 

***Ensure each icon has a unique name and property mapping within the IMX path to avoid conflicts!***

### Icon Definition

We use the snippets above to create all possible icons for the InsulatedJoint.

```python
from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconEntity import IconEntity, IconSvgGroup

entities_path = "InsulatedJoint"
imx_version = ImxVersionEnum.v500

insulated_joint_entities_v500 = [
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="InsulatedJoint",
        properties={},
        icon_groups=[
            IconSvgGroup("insulatedJoint"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="InsulatedJointLeft",
        properties={"rail": "LeftRail"},
        icon_groups=[
            IconSvgGroup("insulatedJoint"),
            IconSvgGroup("insulatedJoint-left"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="InsulatedJointRight",
        properties={"rail": "RightRail"},
        icon_groups=[
            IconSvgGroup("insulatedJoint"),
            IconSvgGroup("insulatedJoint-right"),
        ],
    ),
    IconEntity(
        imx_version=imx_version,
        imx_path=entities_path,
        icon_name="InsulatedJointBoth",
        properties={"rail": "Both"},
        icon_groups=[
            IconSvgGroup("insulatedJoint"),
            IconSvgGroup("insulatedJoint-left"),
            IconSvgGroup("insulatedJoint-right"),
            # optional translate SVG group if needed
            # IconSvgGroup("insulatedJoint-left", "translate(4.25, 0)")
        ],
    ),
]
```

### Property Mapping

The core concept is to identify the best match by sending all flattened properties to the service. 
Unique combinations of properties are required to achieve accurate matching. 
For nested node elements, we utilize an IMX path, similar to how sub-objects are handled.


1. **Send Flattened IMX Properties**  
   All IMX properties are flattened and sent to the service for processing.

2. **Match Defined Mappings**  
   The system evaluates all predefined mappings. If a match is found, the corresponding items are added to the results list.

3. **Prioritize Best Matches**  
   At the end of the evaluation, the system selects the match with the highest number of matching properties to ensure the most accurate result.


***This process should result in exactly **one match**. This requirement should be taken into account when designing icon sets, ensuring that properties are distinct enough to avoid ambiguity.***


### Sub Objects

Sub-object icons are determined using the **puic** attribute as a key. 
If a nested element also contains a **puic** attribute, it is considered a sub-object. 
Each sub-object is represented with its own unique icon.


In the case of sub-objects, sometimes we can project icon over a other icon. The overlap of these icons will create a unique new icon. 
For example, we can combine the `Signal.IlluminatedSign` and `Signal` icon and it will form a combined icon.

!!! warning "Sub Object icons limitations"
    
    Geometric representations in the data or different interpretations of them can lead to strange icons. 
    Therefore, we plan to implement additional properties to generate a complete icon based on derived information.


### IMX Versions
We support specific IMX versions. When a new version is released, it must be explicitly implemented to ensure compatibility and functionality.

The icon definition example provided above corresponds to IMX v5.0.0. For earlier versions, such as v1.2.4, the mappings and icons remain unchanged. 
In these cases, we duplicate the relevant files and change the `imx_version` to reflect the specific version.

Some IMX version does have minor changes that could not be noticed. so each individual icon is essential to ensure accuracy.

### Assemble Complex Icons 

For icons with many variations, consider using methods to stamp SVG snippets onto existing icons. 
Below is a example of adding Danger Signs to a existing list of signals.

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

## Add Icons to the Icon Library

After creating icons, include them in `icon_library.py` by importing and adding them to `ICON_DICT`. The dictionary key is the IMX path.
Now that everything is set up, when running the documentation, the icons should be visible within the generated docs. 

Below is a example of the signals part of the icon library.

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

## Test Icons

It is important to test each icon that will be added to the project. We should build docs and check it out. 
Additionally, when configuring an icon (or set of icons), it's helpful to render the icons to visually verify their appearance.

1. Run `hatch run test` in the terminal to ensure 100% coverage.
2. Verify the generated documentation includes the created icons.
3. Optionally, run `create_all_icons.py` to generate SVG files in the root `icon_renders` folder.
