import os

from app.generate_page import generate_page


def generate_pages_recursive(content_dir_path, template_path, dest_dir_path):
    files = os.listdir(content_dir_path)
    for file in files:
        filepath = os.path.join(content_dir_path, file)
        if os.path.isfile(filepath) and file.endswith('.md'):
            generate_page(
                filepath,
                template_path,
                os.path.join(dest_dir_path, f"{file[:-3]}.html")
            )
        elif not os.path.isfile(filepath):
            generate_pages_recursive(
                filepath,
                template_path,
                os.path.join(dest_dir_path, file)
            )
