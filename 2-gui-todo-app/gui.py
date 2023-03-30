from todo import todo
from utils.time import get_current_date_and_time
import PySimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter to-do')
add_button = sg.Button('Add')

layout = [
    [label],
    [input_box, add_button]
]

window = sg.Window('To-do app', layout=layout)
window.read()
window.close()
