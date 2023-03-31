from todo import todo
from utils.time import get_current_date_and_time
import PySimpleGUI as sg
from gui import app


def main():
    while True:
        event, values = app.window.read()

        match event:

            case 'Add':
                new_todo = values['todo'] + '\n'
                todos = todo.add_todo(todo_item=new_todo)
                app.window['todos'].update(values=todos)

            case 'Edit':
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = todo.edit_todo(todo_to_edit=todo_to_edit, new_todo=new_todo)
                app.window['todos'].update(values=todos)

            case 'todos':
                app.window['todo'].update(value=values['todos'][0])

            case sg.WIN_CLOSED:
                break

    app.window.close()


if __name__ == "__main__":
    main()
