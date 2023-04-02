import os


def read_todo(filename):
    """
    Read todos.txt file and return list of todos
    Params:
        filename - filename to read the content from there
    """
    try:
        with open(filename, 'r') as file:
            todos = file.readlines()

        return todos
    except FileNotFoundError:
        with open(filename, 'w'):
            pass


def write_todo(filename, content):
    """
    Overwrite todos.txt file with new todos list
    Params:
        filename - filename to write the content in there
        content - list of your content
    """
    with open(filename, 'w') as file:
        file.writelines(content)


def get_file(file_path):
    """
    Return current path to file
    Params:
        file_path: Example - '..files/todos.txt'
    """
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    image_path = os.path.join(current_directory, file_path)
    return image_path
