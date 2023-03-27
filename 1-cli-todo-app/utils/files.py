def read_todo(filename):
    """Read todos.txt file and return list of todos"""
    with open(filename, 'r') as file:
        todos = file.readlines()

    return todos


def write_todo(filename, content):
    """Overwrite todos.txt file with new todos list"""
    with open(filename, 'w') as file:
        file.writelines(content)
