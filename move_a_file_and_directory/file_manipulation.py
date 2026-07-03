import os

def validate_path(path):
    if not os.path.isdir(path) and not os.path.isfile(path):
        raise FileNotFoundError(f"{path} is not a valid path.")

def determine_destination(source, destination):
    basename_of_path = os.path.basename(source)
    destination += ("\\" + basename_of_path)
    return destination


def move_source(source, destination):
    if os.path.exists(destination):
        print("The chosen file.txt/directory already exists.")
    else:
        os.replace(source, destination)
        print(f"{source} -> {destination}")