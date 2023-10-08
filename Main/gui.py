import function
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter task")
add_button = sg.Button("Add Task")

window = sg.Window('My To-Do App', layout=[[label], [add_button, input_box]])
window.read()
print('hello')
window.close()
