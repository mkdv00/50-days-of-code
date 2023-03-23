todos: list = []


while True:
    user_action: str = input('Type "add", "show" or "exit": ')
    user_action = user_action.lower().strip()

    match user_action:
        case 'add' | 'create':
            todo: str = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            if len(todos) >= 1:
                print('Todos now:')

                for todo in enumerate(todos, start=1):
                    print(f"{todo[0]}: {todo[1].capitalize()}.")
            else:
                print('Nothing to show.')
        case 'exit' | 'quit':
            break
        case _:
            print('Hey, you entered an unknown command.')

print('Bye!')
