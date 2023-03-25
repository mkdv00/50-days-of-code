from utils import files

todos_file = 'files/todos.txt'


while True:
    user_action = input('Type "add", "show", "edit", "complete" or "exit": ')
    user_action = user_action.lower().strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + '\n'

            todos = files.read_todo(todos_file)
            todos.append(todo.capitalize())

            files.write_todo(todos_file, todos)

        case 'show':
            todos = files.read_todo(todos_file)

            if len(todos) >= 1:
                for index, todo_item in enumerate(todos, start=1):
                    todo_item = todo_item.strip('\n')
                    template = f"{index}: {todo_item}."
                    print(template)
            else:
                print('Nothing to show.')

        case 'edit':
            todo_index = int(input('Number of the todo to edit: ')) - 1
            new_todo = input('Enter new todo: ')
            todos[todo_index] = new_todo

        case 'complete':
            todo_index = int(input('Number of the todo to complete: ')) - 1
            print(f"Completed: {todos.pop(todo_index)}")

        case 'exit':
            break

        case _:
            print('Hey, you entered an unknown command.')

print('Bye!')
