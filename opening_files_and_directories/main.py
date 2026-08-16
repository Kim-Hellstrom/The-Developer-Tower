import configure_url
from configure_url import (format_path,
                           check_if_path,
                           check_if_file_or_dir,
                           open_path)

### This program is automated script to open up files for the user, as long as the user provides an absolute path.

# Initializers
welcome_message = ("This program will detect if the PATH you provide leads to a directory or a file\n"
                   "exit = quit the program\n")

# Program begins here
print(welcome_message)
# Check user input
while True:
    user_input = input("Enter absolute PATH or exit: ")
    if user_input == "exit":
        break
    if user_input == "":
        print("Please provide a path or exit")

    # Define Path
    path = format_path(user_input)
    if not check_if_path(path):
        print("The PATH provided does not exist")
        continue
    message = check_if_file_or_dir(path)
    print(message)

    # Path manipulation
    open_path(path)