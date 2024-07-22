import os
from app.markdown_to_htmlnode import markdown_to_htmlnode
from app.extract_title import extract_title


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(
        f"Generating page from '{from_path}' to '{
            dest_path}' using '{template_path}'"
    )
    file_content = read_file_content(from_path)
    template_content = read_file_content(template_path)
    htmlnode = markdown_to_htmlnode(file_content)
    htmlstring = htmlnode.to_html()
    title = extract_title(file_content)
    dest_content = template_content.replace(
        "{{ Title }}", title
    ).replace(
        "{{ Content }}", htmlstring
    )
    dest_dirs = os.path.dirname(dest_path)
    os.makedirs(dest_dirs, exist_ok=True)
    with open(dest_path, "w") as dest_file:
        dest_file.write(dest_content)
    print("Successfully generated html file.")


def read_file_content(from_path):
    if not os.path.exists(from_path):
        raise ValueError(f'Could not find the file at {from_path}')
    with open(from_path, 'r') as file:
        return file.read()
