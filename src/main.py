import os
from app.copy_static import copy_static
from app.generate_pages_recursive import generate_pages_recursive


def main():
    copy_static()
    cwd = os.getcwd()
    from_path = os.path.join(cwd, 'content')
    template_path = os.path.join(cwd, 'template.html')
    dest_path = os.path.join(cwd, 'public')
    generate_pages_recursive(from_path, template_path, dest_path)


main()
