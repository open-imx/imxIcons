import glob
import os
import shutil
from pathlib import Path

import pytest

from create_icon_library_pages import (
    remove_existing_icon_library_section,
    get_icon_library_index,
    get_nav_index,
    get_mkdocs_yml_as_lines,
    generate_markdowns,
    update_mkdocs_yml
)


def clean_generated_folder(directory_path: Path):
    """
    Removes all files and directories in the specified folder, except for .auto_generated_content.

    :param directory_path: Path to the folder to clean.
    """
    for filename in os.listdir(directory_path):
        file_path = directory_path / filename

        # Skip the .auto_generated_content file
        if filename != '.auto_generated_content':
            try:
                if file_path.is_dir():
                    shutil.rmtree(file_path)  # Remove the directory and its contents
                else:
                    file_path.unlink()  # Remove the file
            except Exception as e:
                print(f"Error removing {file_path}: {e}")


def get_generated_directory_path() -> Path:
    """Returns the path of the generated directory based on the current directory."""
    current_directory = Path(__file__).parent
    if 'tests' in str(current_directory):  # Adjust this condition based on where the test is run from
        return current_directory / Path('../docs/generated')
    return Path('docs/generated')


def get_mkdocs_yml_path() -> Path:
    """Returns the path of the mkdocs.yml file based on the current directory."""
    current_directory = Path(__file__).parent
    if 'tests' in str(current_directory):  # Adjust this condition based on where the test is run from
        return current_directory / Path("../mkdocs.yml")
    return Path("mkdocs.yml")


def test_generate_icon_library():
    directory_path = get_generated_directory_path()
    clean_generated_folder(directory_path)

    contents = list(directory_path.iterdir())
    assert len(contents) == 1, f"Expected 1 item, found {len(contents)}"
    assert contents[0].is_file(), "The item is not a file"
    assert contents[0].name == ".auto_generated_content", f"Expected '.auto_generated_content', found {contents[0].name}"
    assert not any(item.is_dir() for item in contents), "There are subdirectories present"

    mkdocs_yml = get_mkdocs_yml_path()

    lines = get_mkdocs_yml_as_lines(mkdocs_yml)
    nav_index = get_nav_index(lines)
    if nav_index is None:
        raise ValueError("No 'nav:' section found in mkdocs.yml.")

    icon_library_index = get_icon_library_index(lines)
    remove_existing_icon_library_section(lines, icon_library_index)

    with mkdocs_yml.open("w") as file:
        file.writelines(lines)

    lines = get_mkdocs_yml_as_lines(mkdocs_yml)
    assert '  - Icon Library:\n' not in lines, "Should not have a Icon Library in nav"

    generate_markdowns(directory_path)
    md_files = glob.glob(str(directory_path / '**' / '*.md'), recursive=True)
    assert len(md_files) > 0, f"No .md files found in {directory_path}"

    # Update mkdocs.yml and verify changes
    update_mkdocs_yml()
    lines = get_mkdocs_yml_as_lines(mkdocs_yml)
    assert '  - Icon Library:\n' in lines, "Icon Library should be present in nav"
