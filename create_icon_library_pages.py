import os
from pathlib import Path
from imxIcons.domain.supportedImxVersions import ImxVersionEnum
from imxIcons.iconService import IconService
from imxIcons.domain.icon_library import ICON_DICT
from imxIcons.iconServiceModels import IconRequestModel
from jinja2 import Environment, FileSystemLoader
import xml.etree.ElementTree as ET


def add_transformations(svg_string: str, scale: float, translate_x: float = 0, translate_y: float = 0) -> str:
    """
    Adds scale and translation transformations to the SVG content.
    """
    root = ET.fromstring(svg_string)
    if root.tag.lower().endswith('svg'):
        current_transform = root.attrib.get('transform', '')
        new_transform = f"{current_transform} translate({translate_x}, {translate_y}) scale({scale})".strip()
        root.set('transform', new_transform)
    return ET.tostring(root, encoding='unicode', method='xml')


def generate_icon_list(icons, version: str) -> list:
    """
    Generates a list of icon details with transformed SVG content.
    """
    icon_list = []
    for icon in icons:
        svg_content = IconService.get_svg(
            IconRequestModel(imx_path=icon.imx_path, properties=icon.properties, additional_properties=icon.additional_properties),
            ImxVersionEnum[version],
        )
        scaled_svg = add_transformations(svg_content, scale=2.75, translate_x=-90)
        if icon.additional_properties:
            properties = {'imx_path': icon.imx_path} | {'properties': icon.properties} | {'additional_properties': icon.additional_properties}
        else:
            properties = {'imx_path': icon.imx_path} | {'properties': icon.properties}

        icon_list.append({
            "name": icon.icon_name,
            "svg": scaled_svg,
            "properties": properties,
            "raw_code": svg_content
        })
    return icon_list


def generate_markdowns(docs_generated_dir: str):
    """
    Generates markdown files for each icon in the ICON_DICT and saves them to the specified directory.
    """
    ET.register_namespace('', "http://www.w3.org/2000/svg")
    env = Environment(loader=FileSystemLoader('docs/templates'))
    template = env.get_template('icon_library_page.html')

    for imx_path, versions in ICON_DICT.items():
        for version, icons in versions.items():
            version_dir = os.path.join(docs_generated_dir, f"IMX {version}")
            os.makedirs(version_dir, exist_ok=True)

            icon_list = generate_icon_list(icons, version)
            if icon_list:
                md_path = os.path.join(version_dir, f"{imx_path}.md")
                with open(md_path, 'w') as f:
                    f.write(template.render(icons=icon_list))


def check_mkdocs_exists(mkdocs_yml: Path):
    """Checks if the mkdocs.yml file exists."""
    if not mkdocs_yml.exists():
        raise ValueError("mkdocs.yml not found. Please create one before running this script.")


def get_nav_index(lines):
    """Finds the index of the 'nav:' section."""
    return next((i for i, line in enumerate(lines) if line.strip() == "nav:"), None)


def get_icon_library_index(lines):
    """Finds the index of the 'Icon Library' section if it exists."""
    return next((i for i, line in enumerate(lines) if '  - Icon Library:' in line), None)


def remove_existing_icon_library_section(lines, icon_library_index):
    """Removes the existing 'Icon Library' section if it exists."""
    if icon_library_index is not None:
        end_index = icon_library_index + 1
        while end_index < len(lines) and lines[end_index].startswith(" " * 4):
            end_index += 1
        del lines[icon_library_index:end_index]
        print("Removed existing 'Icon Library' section.")

def get_files_by_type(files):
    """Categorize files into path files and tag files."""
    path_files = []
    tag_files = []
    for file in files:
        file_stem = file.stem
        is_tag = any(
            other_file.stem.endswith(f".{file_stem}")
            for other_file in files if other_file != file
        )
        if is_tag:
            tag_files.append(file)
        else:
            path_files.append(file)
    return path_files, tag_files

def format_entries(files, version_name, indent_level):
    """Generate formatted entries for files."""
    indent = "  " * indent_level
    return [
        f"{indent}- {file.stem}: generated/{version_name}/{file.name}\n"
        for file in files
    ]

def create_version_entry(version_dir):
    """Create an entry for a specific version directory."""
    version_name = version_dir.name
    version_entry = f"    - {version_name}:\n"

    files = sorted(version_dir.glob("*.md"))
    path_files, tag_files = get_files_by_type(files)

    path_entries = format_entries(path_files, version_name, indent_level=3)
    if path_entries:
        version_entry += ''.join(path_entries)

    tag_entries = format_entries(tag_files, version_name, indent_level=4)
    if tag_entries:
        version_entry += "      - Child objects by tag:\n" + ''.join(tag_entries)

    return version_entry

def create_new_icon_library_section():
    """Creates a new 'Icon Library' section based on the files in 'docs/generated'."""
    icon_library_section = ["  - Icon Library:\n"]

    for version_dir in sorted(Path("docs/generated").iterdir()):
        if version_dir.is_dir():
            version_entry = create_version_entry(version_dir)
            icon_library_section.append(version_entry)

    return icon_library_section

def get_reference_index(lines):
    """Finds the index of the '- Reference:' section."""
    below_section = "- Reference:"
    return next((i for i, line in enumerate(lines) if line.strip().startswith(below_section)), None)


def insert_icon_library_section(lines, reference_index, icon_library_section):
    """Inserts the new 'Icon Library' section after the '- Reference:' section."""
    reference_indent = 2
    insert_index = reference_index + 1
    while insert_index < len(lines) and lines[insert_index].startswith(" " * (reference_indent + 2)):
        insert_index += 1

    icon_library_section_indented = [
        ' ' * (reference_indent - 2) + line for line in icon_library_section
    ]
    lines[insert_index:insert_index] = icon_library_section_indented

def get_mkdocs_yml_as_lines(mkdocs_yml: Path) -> list[str]:
    check_mkdocs_exists(mkdocs_yml)

    with mkdocs_yml.open("r") as file:
        lines = file.readlines()
    return lines

def update_mkdocs_yml():
    """Main function to update the mkdocs.yml file with a new 'Icon Library' section."""

    mkdocs_yml = Path("mkdocs.yml")

    lines = get_mkdocs_yml_as_lines(mkdocs_yml)

    nav_index = get_nav_index(lines)
    if nav_index is None:
        raise ValueError("No 'nav:' section found in mkdocs.yml.")

    icon_library_index = get_icon_library_index(lines)
    remove_existing_icon_library_section(lines, icon_library_index)

    icon_library_section = create_new_icon_library_section()

    reference_index = get_reference_index(lines)
    if reference_index is None:
        raise ValueError("No '- Reference:' section found in mkdocs.yml.")

    insert_icon_library_section(lines, reference_index, icon_library_section)

    with mkdocs_yml.open("w") as file:
        file.writelines(lines)

    print("Updated mkdocs.yml with new 'Icon Library' section.")


if __name__ == "__main__":
    docs_dir = "docs/generated"
    os.makedirs(docs_dir, exist_ok=True)
    generate_markdowns(docs_dir)
    update_mkdocs_yml()
