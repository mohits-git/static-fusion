import os
import shutil


def copy_files(files, source, destination):
    for file in files:
        filepath = os.path.join(source, file)
        if os.path.isfile(filepath):
            shutil.copy(filepath, destination)
            print(f"FILE '{filepath}' COPIED TO '{destination}'")
        else:
            dir_source = filepath
            dir_destination = os.path.join(destination, file)
            os.mkdir(dir_destination)
            print(f"new directory created - '{dir_destination}'")
            dir_files = os.listdir(dir_source)
            copy_files(dir_files, dir_source, dir_destination)


def copy_static():
    try:
        print('Copying static/ to public/')
        destination = os.path.join(os.getcwd(), 'public/')
        source = os.path.join(os.getcwd(), 'static/')
        if not os.path.exists(source):
            raise ValueError("Static directory doesn't exist")
        if os.path.exists(destination):
            shutil.rmtree(destination)
            print(f"old public/ dir removed - {destination}")
        os.mkdir(destination)
        print(f"new public/ directory created - {destination}")
        files = os.listdir(source)
        copy_files(files, source, destination)
    except ValueError as error:
        print(error.args[0])
    except Exception as error:
        print("Something went wrong")
        print(error)
