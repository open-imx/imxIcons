import os
import ast
from pathlib import Path


SRC_DIR = "imxIcons/domain"
DOCS_DIR = "docs/generated"


TEMPLATE = """
# {class_name}

**File:** `{file_path}`

**Docstring:**

{docstring}

## Methods

{methods}
"""


def extract_classes(file_path):
    # TODO: make get all versions, icons and properties
    """Extract class definitions from a Python file."""
    with open(file_path, "r") as file:
        tree = ast.parse(file.read(), filename=file_path)

    classes = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            docstring = ast.get_docstring(node) or "No docstring available."
            methods = [
                f"- `{n.name}()`" for n in node.body if isinstance(n, ast.FunctionDef)
            ]
            classes.append({
                "name": node.name,
                "docstring": docstring,
                "methods": "\n".join(methods),
            })
    return classes


def create_markdown(class_data, file_path):
    """Generate a Markdown file for a class."""
    # TODO: make nice template left a icon svg, to the right the properties
    for cls in class_data:
        class_name = cls["name"]
        docstring = cls["docstring"]
        methods = cls["methods"]
        output_file = Path(DOCS_DIR) / f"{class_name}.md"

        with open(output_file, "w") as md_file:
            md_file.write(
                TEMPLATE.format(
                    class_name=class_name,
                    file_path=file_path,
                    docstring=docstring,
                    methods=methods,
                )
            )
        print(f"Generated: {output_file}")







def crawl_directory(src_dir):
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                class_data = extract_classes(file_path)
                if class_data:
                    create_markdown(class_data, file_path)


def update_mkdocs_yml():

    mkdocs_yml = Path("mkdocs.yml")
    if not mkdocs_yml.exists():
        raise ValueError("mkdocs.yml not found. Please create one before running this script.")

    with mkdocs_yml.open("r") as file:
        lines = file.readlines()

    # Find nav section
    nav_index = next((i for i, line in enumerate(lines) if line.strip() == "nav:"), None)
    if nav_index is None:
        raise ValueError("No 'nav:' section found in mkdocs.yml.")

    # Remove 'Icon Library' section (if it exists)
    icon_library_index = next(
        (i for i, line in enumerate(lines) if '  - Icon Library:' in line ),
        None,
    )
    if icon_library_index is not None:
        # Find end of 'Icon Library' section by detecting the next non-indented line
        end_index = icon_library_index + 1
        while end_index < len(lines) and lines[end_index].startswith(" " * 4):
            end_index += 1

        del lines[icon_library_index:end_index]
        print("Removed existing 'Icon Library' section.")

    # Create new 'Icon Library' entries
    library_entries = [
        f"      - {file.stem}: generated\\{file.name}\n"
        for file in Path(DOCS_DIR).glob("*.md")
    ]
    icon_library_section = ["  - Icon Library:\n"] + library_entries

    # Find the line after the last `- Reference:` entry
    below_section = "- Reference:"
    reference_index = next(
        (i for i, line in enumerate(lines) if line.strip().startswith(below_section)),
        None,
    )
    if reference_index is None:
        raise ValueError("No '- Reference:' section found in mkdocs.yml.")

    # Determine the indentation level
    reference_indent = 2

    # Insert the new 'Icon Library' section
    insert_index = reference_index + 1
    while insert_index < len(lines) and lines[insert_index].startswith(" " * (reference_indent + 2)):
        insert_index += 1

    # Adjust the indent
    icon_library_section_indented = [
        ' ' * (reference_indent - 2) + line for line in icon_library_section
    ]

    # Insert the new 'Icon Library'
    lines[insert_index:insert_index] = icon_library_section_indented

    with mkdocs_yml.open("w") as file:
        file.writelines(lines)

    print("Updated mkdocs.yml with new 'Icon Library' section.")



if __name__ == "__main__":
    # Ensure the output directory exists
    os.makedirs(DOCS_DIR, exist_ok=True)

    # Crawl the source directory and generate docs
    crawl_directory(SRC_DIR)

    # Update mkdocs.yml
    update_mkdocs_yml()