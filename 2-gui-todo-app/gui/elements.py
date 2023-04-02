import PySimpleGUI as sg

from todo import todo


class App:

    def __init__(self, title='Example', font=('Helvetica', 16)):
        """
        Args:
            title='Example', font=('Helvetica', 16) - Default values
        Contains:
            title, font, input label, input, add_button, list_box, edit_button,
            layout, window
        """
        sg.theme('Black')

        self.title = title
        self.font = font

        self.clock = sg.Text('', key='clock')
        self.label = sg.Text('Type in a to-do')
        self.input_box = sg.InputText(tooltip='Enter to-do', key='todo')
        self.add_button = sg.Button('Add')

        self.list_box = sg.Listbox(values=todo.get_todos(), key='todos',
                                   enable_events=True, size=(45, 10))

        self.edit_button = sg.Button('Edit')
        self.complete_button = sg.Button('Complete')
        self.exit_button = sg.Button('Exit')

        self.layout = [
            [self.clock],
            [self.label],
            [self.input_box, self.add_button],
            [self.list_box, self.edit_button, self.complete_button],
            [self.exit_button]
        ]

        self.window = sg.Window(title=self.title,
                                layout=self.layout,
                                font=self.font)
