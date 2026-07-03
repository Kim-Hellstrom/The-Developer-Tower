from file_manipulation import (validate_path,
                               determine_destination,
                               move_source)

while True:
    try:
        # Checks source path
        source = input("Enter the source path or exit: ")
        if source == "exit":
            break
        validate_path(source)

        # Checks destination path
        destination = input("Enter the destination path or exit: ")
        if destination == "exit":
            break
        destination = determine_destination(source, destination)

        # Move source
        move_source(source, destination)

    except FileNotFoundError:
        print(f"{source} not found.")
    except PermissionError:
        print(f"{source} wasn't allowed to be moved.")