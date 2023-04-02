import os


def read_todo(filename):
    """Read todos.txt file and return list of todos"""
    with open(filename, 'r') as file:
        todos = file.readlines()

    return todos


def write_todo(filename, content):
    """Overwrite todos.txt file with new todos list"""
    with open(filename, 'w') as file:
        file.writelines(content)


def get_file(file_path):
    """
    Return current path to file
    Params:
        file_path: Example - '../images/app/add.png'
    """
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    image_path = os.path.join(current_directory, file_path)
    return image_path
