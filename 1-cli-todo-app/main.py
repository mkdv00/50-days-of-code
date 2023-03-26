from todo import todo


def main():
    while True:
        user_action = input('Type "add", "show", "edit", "complete" or "exit": ')
        user_action = user_action.lower()

        if 'add' in user_action:
            todo.add_todo(user_action=user_action)
        elif 'show' in user_action:
            todo.show_todos()
        elif 'edit' in user_action:
            todo.edit_todo(user_action=user_action)
        elif 'complete' in user_action:
            todo.complete_todo(user_action=user_action)
        elif 'exit' in user_action:
            break
        else:
            print('Hey, you entered an unknown command.')

    print('Bye!')


if __name__ == '__main__':
    main()
