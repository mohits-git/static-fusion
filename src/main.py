import os
from app.copy_static import copy_static
from app.generate_page import generate_page


def main():
    copy_static()
    cwd = os.getcwd()
    from_path = os.path.join(cwd, 'content/index.md')
    template_path = os.path.join(cwd, 'template.html')
    dest_path = os.path.join(cwd, 'public/index.html')
    generate_page(from_path, template_path, dest_path)


main()
