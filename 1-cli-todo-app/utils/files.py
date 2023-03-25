def read_todo(filename):
    with open(filename, 'r') as file:
        todos = file.readlines()

    return todos


def write_todo(filename, content):
    with open(filename, 'w') as file:
        file.writelines(content)
