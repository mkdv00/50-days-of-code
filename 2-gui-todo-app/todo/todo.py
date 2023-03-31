from utils import files


class Todo:

    def __init__(self, filename):
        self.filename = filename

    def add_todo(self, todo_item):
        """Add todos item in file"""
        todos = files.read_todo(self.filename)
        todos.append(todo_item.lstrip().capitalize())

        files.write_todo(self.filename, todos)
        return todos

    def get_todos(self):
        """Get all todos from the file and improve it for printing"""
        todos = files.read_todo(self.filename)
        return todos

    def edit_todo(self, todo_to_edit, new_todo):
        """Overwrite the todos file"""
        todos = files.read_todo(self.filename)
        index = todos.index(todo_to_edit)

        todos[index] = new_todo + '\n'

        files.write_todo(self.filename, todos)
        return todos

    def complete_todo(self, user_action):
        """Complete todos item"""
        try:
            todo_to_complete = user_action.replace('complete', '')
            todo_index = int(todo_to_complete.lstrip()) - 1

            todos = files.read_todo(self.filename)

            todo_to_remove = todos[todo_index].strip('\n')
            todos.pop(todo_index)

            files.write_todo(self.filename, todos)

            print(f"Todo '{todo_to_remove}' was removed from the list.")
        except IndexError:
            print(f"Your todo does not exists.")
