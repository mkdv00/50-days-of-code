from todo import todo
from utils.time import get_current_date_and_time
import PySimpleGUI as sg
from gui import app


def main():
    while True:
        event, values = app.window.read(timeout=10)
        app.window['clock'].update(value=get_current_date_and_time())

        match event:

            case 'Add':
                todos = todo.add_todo(event_value=values)
                app.window['todos'].update(values=todos)

            case 'Edit':
                todos = todo.edit_todo(event_value=values)
                app.window['todos'].update(values=todos)

            case 'Complete':
                todos = todo.complete_todo(event_value=values)
                app.window['todos'].update(values=todos)
                app.window['todo'].update(value='')

            case 'Exit':
                break

            case sg.WIN_CLOSED:
                break

    app.window.close()


if __name__ == "__main__":
    main()
