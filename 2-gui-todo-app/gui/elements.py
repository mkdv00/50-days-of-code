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
        self.title = title
        self.font = font

        self.label = sg.Text('Type in a to-do')
        self.input_box = sg.InputText(tooltip='Enter to-do', key='todo')
        self.add_button = sg.Button('Add')

        self.list_box = sg.Listbox(values=todo.get_todos(), key='todos',
                                   enable_events=True, size=(45, 10))

        self.edit_button = sg.Button('Edit')

        self.layout = [
            [self.label],
            [self.input_box, self.add_button],
            [self.list_box, self.edit_button]
        ]

        self.window = sg.Window(title=self.title,
                                layout=self.layout,
                                font=self.font)
