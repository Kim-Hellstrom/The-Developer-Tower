import os

# Cleans the user input to a viable URL
def format_path(path):
    if path.startswith('"') and path.endswith('"'):
        path = path[1:-1]
    return path

# Checks that the PATH exist
def check_if_path(path):
    if os.path.exists(path):
        return True
    else:
        return False

# Confirms if it is a file or a directory
def check_if_file_or_dir(path):
    if os.path.isfile(path):
        return "This is a file"
    elif os.path.isdir(path):
        return "This is a directory"
    else:
        return "What the hell did you try to create"

def open_path(path):
    os.startfile(path)