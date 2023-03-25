from utils import files


class Todo:

    def __init__(self, filename):
        self.filename = filename

    def add_todo(self):
        """Add todos item in file"""
        todo = input('Enter a todo: ') + '\n'

        todos = files.read_todo(self.filename)
        todos.append(todo.capitalize())

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

    def edit_todo(self):
        """Overwrite the todos file"""
        todo_index = int(input('Number of the todo to edit: ')) - 1

        todos = files.read_todo(self.filename)

        new_todo = input('Enter new todo: ')
        todos[todo_index] = new_todo + '\n'

        files.write_todo(self.filename, todos)

    def complete_todo(self):
        """Complete todos item"""
        user_todo = int(input('Number of the todo to complete: '))

        todos = files.read_todo(self.filename)

        todo_index = user_todo - 1
        todo_to_remove = todos[todo_index].strip('\n')
        todos.pop(todo_index)

        files.write_todo(self.filename, todos)

        print(f"Todo {todo_to_remove} was removed from the list.")
