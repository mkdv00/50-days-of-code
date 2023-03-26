from utils import files


class Todo:

    def __init__(self, filename):
        self.filename = filename

    def add_todo(self, user_action):
        """Add todos item in file"""
        todo = user_action.replace('add', '') + '\n'

        todos = files.read_todo(self.filename)
        todos.append(todo.lstrip().capitalize())

        files.write_todo(self.filename, todos)

    def show_todos(self):
        """Show all todos from the file"""
        todos = files.read_todo(self.filename)

        if len(todos) >= 1:
            for index, todo_item in enumerate(todos, start=1):
                todo_item = todo_item.strip('\n')
                template = f"{index}: {todo_item}."
                print(template)
        else:
            print('Nothing to show.')

    def edit_todo(self, user_action):
        """Overwrite the todos file"""
        todo_to_edit = user_action.replace('edit', '')
        todo_index = int(todo_to_edit.lstrip()) - 1

        todos = files.read_todo(self.filename)

        old_todo = todos[todo_index].strip('\n')
        new_todo = input('Enter new todo: ')

        print(f"Todo before edit: {old_todo}")
        print(f"Todo after edit: {new_todo}")

        todos[todo_index] = new_todo + '\n'

        files.write_todo(self.filename, todos)

    def complete_todo(self, user_action):
        """Complete todos item"""
        todo_to_complete = user_action.replace('complete', '')
        todo_index = int(todo_to_complete.lstrip()) - 1

        todos = files.read_todo(self.filename)

        todo_to_remove = todos[todo_index].strip('\n')
        todos.pop(todo_index)

        files.write_todo(self.filename, todos)

        print(f"Todo '{todo_to_remove}' was removed from the list.")
