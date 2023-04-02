from utils import files


class Todo:

    def __init__(self, filename):
        self.filename = filename

    def add_todo(self, event_value):
        """Add todos item in file"""
        todos = files.read_todo(self.filename)

        new_todo = event_value['todo'] + '\n'

        todos.append(new_todo.lstrip().capitalize())
        files.write_todo(self.filename, todos)

        return todos

    def get_todos(self):
        """Get all todos from the file and improve it for printing"""
        todos = files.read_todo(self.filename)
        return todos

    def edit_todo(self, event_value):
        """Overwrite the todos file"""
        try:
            todos = files.read_todo(self.filename)

            todo_to_edit = event_value['todos'][0]
            index = todos.index(todo_to_edit)

            new_todo = event_value['todo']

            todos[index] = new_todo + '\n'
            files.write_todo(self.filename, todos)

            return todos
        except IndexError:
            print(f"Your todo does not exists.")

    def complete_todo(self, event_value):
        """Complete todos item"""
        try:
            todos = files.read_todo(self.filename)

            todo_to_complete = event_value['todos'][0]
            index = todos.index(todo_to_complete)

            todos.pop(index)
            files.write_todo(self.filename, todos)

            return todos
        except IndexError:
            print(f"Your todo does not exists.")
