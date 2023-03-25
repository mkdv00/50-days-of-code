from todo import todo


while True:
    user_action = input('Type "add", "show", "edit", "complete" or "exit": ')
    user_action = user_action.lower().strip()

    match user_action:
        case 'add':
            todo.add_todo()
        case 'show':
            todo.show_todos()
        case 'edit':
            todo.edit_todo()
        case 'complete':
            todo.complete_todo()
        case 'exit':
            break
        case _:
            print('Hey, you entered an unknown command.')

print('Bye!')
