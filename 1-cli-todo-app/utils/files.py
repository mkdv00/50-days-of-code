def read_todo(filename):
    file = open(filename, 'r')
    todos = file.readlines()
    file.close()

    return todos


def write_todo(filename, content):
    file = open(filename, 'w')
    file.writelines(content)
    file.close()
