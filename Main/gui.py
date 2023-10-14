import function as fn
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter task")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=fn.get_todos("text.txt"), key='todos',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App', layout=[[label], [add_button, input_box], 
                   [list_box, edit_button]], font=('Arial', 10))



#Keep application open until it is intentionally closed
while True:
    event, value = window.read()
    print(event)
    if event == "Add": 
        todos = fn.get_todos("text.txt")
        todos.append(value[0] + "\n")
        fn.write_todos("text.txt", todos)
        print(event, value)
    
    elif event == "Edit":
        todos = fn.get_todos()
        print(todos)
        print(event)
        print(value)
    elif event == sg.WIN_CLOSED:
        break

window.close()
