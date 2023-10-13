import function as fn
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter task")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [add_button, input_box]], font=('Arial', 10))




while True:
    event, value = window.read()
    if event == "Add": 
        todos = fn.get_todos("text.txt")
        todos.append(value[0] + "\n")
        fn.write_todos("text.txt", todos)
    elif event == sg.WIN_CLOSED:
        break
    else:
        break

window.close()
