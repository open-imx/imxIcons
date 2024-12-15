
# Design parts
This section provides an overview of the design considerations and guidelines for creating icons.

## Design Guidelines

- **Rotation**: The design should be rotated 90° clockwise from North.
- **Insertion Point**: The insertion point is defined at coordinates `(x0, y0)`, a stamp will be automatically generated within the icon.
- **Classic Drawings**: Keep the design aligned with traditional schematic representations, maintaining familiarity for users.

## Design Parts Guidelines

For further details, refer to the icon configuration documentation. Key considerations for designing an icon include:


- **IMX Path-like Object**: The icon should represent an IMX path-like object. 
- **Modular Structure**: The design should be modular, enabling the reuse of parts.
- **Uniqueness**: Each part should be unique, defined by a specific set of IMX properties to avoid redundancy.
- **Specificity**: The design should prioritize specific over complex elements, ensuring simplicity and clarity.
- **Colors and GIS Parameters**: Design should account for color schemes and parameters used in (Q)GIS applications.

!!! note ""
    
    **Additional Properties**: Additional properties should be implemented to include subobjet context in a icon.
    This is a future feature.


## SVG Tags
If an icon has dynamic aspects, we can add classes to it. These classes can be used in combination with the SVG group name to implement behavior in the frontend. 
Please note that the current classes are just a concept and may evolve over time. If you have any suggestions or ideas, feel free to share them.

## Other Icon View
There may be instances where different perspectives require a different icon for the same IMX object or property combination. 
Although we have not yet implemented a solution for this, one possible approach could be to introduce an additional domain. 
If this situation arises, please make sure to reach out to us on Discord for further discussion.

## Tips:

List of apps that can help you out.

- **Edit SVG**: You can use [Boxy](https://boxy-svg.com/) for editing SVG files.
- **Clean SVG**: [SVGOMG](https://svgomg.net/) is a great tool for optimizing and cleaning SVG files.
