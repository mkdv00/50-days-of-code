import PySimpleGUI as sg
from utils import files

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
        self.list_box = sg.Listbox(values=todo.get_todos(), key='todos',
                                   enable_events=True, size=(45, 10))

        self.add_button = sg.Button(size=2, image_source=files.get_file('../images/app/add.png'), key='Add',
                                    mouseover_colors='LightBlue2', tooltip='Add to-do')
        self.edit_button = sg.Button('Edit', tooltip='Choose to-do from the list and type new to-do in input')
        self.complete_button = sg.Button(image_source=files.get_file('../images/app/complete.png'), key='Complete',
                                         mouseover_colors='LightBlue2',
                                         tooltip='Choose to-do to and press this button to complete')
        self.exit_button = sg.Button('Exit')

        self.layout = [
            [self.clock],
            [self.label],
            [self.input_box, self.add_button, self.complete_button],
            [self.list_box, self.edit_button],
            [self.exit_button]
        ]

        self.window = sg.Window(title=self.title,
                                layout=self.layout,
                                font=self.font)
