from todo import todo
from utils.time import get_current_date_and_time


def main():
    now = get_current_date_and_time()
    print(f"It's {now}")

    while True:
        user_action = input('Type "add", "show", "edit", "complete" or "exit": ')
        user_action = user_action.lower()

        if user_action.startswith('add'):
            todo.add_todo(user_action=user_action)
        elif user_action.startswith('show'):
            todo.show_todos()
        elif user_action.startswith('edit'):
            todo.edit_todo(user_action=user_action)
        elif user_action.startswith('complete'):
            todo.complete_todo(user_action=user_action)
        elif user_action.startswith('exit'):
            break
        else:
            print('Hey, you entered an unknown command.')

    print('Bye!')


if __name__ == '__main__':
    main()
