import function as fn
import PySimpleGUI as sg
import os

if not os.path.exists("text.txt"):
    with open("text.txt", 'w') as file:
        pass

sg.theme("DarkGray8")

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter task", key='todo')
add_button = sg.Button("add", button_color="LightBlue", mouseover_colors=("white"), key="Add")

list_box = sg.Listbox(values=fn.get_todos("text.txt"), key='todos',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit", key="Edit")
complete_button = sg.Button("Complete", key="Complete")

exit_button = sg.Button("Exit", key="Exit")

window = sg.Window('My To-Do App', layout=[[label], 
                                           [add_button, input_box], 
                                           [list_box, edit_button, complete_button],
                                           [exit_button]], 
                                           font=('Arial', 10))



#Keep application open until it is intentionally closed
while True:

    event, value = window.read()

    if event == "Add": 
        todos = fn.get_todos("text.txt")
        todos.append(value['todo'] + "\n")
        fn.write_todos("text.txt", todos)
        window['todos'].update(values=todos)

    elif event == "todos":
        window['todo'].update(value=value['todos'][0][:-1])
        todos = fn.get_todos()
        todos_index = todos.index(value["todos"][0])
        todo_value = value["todos"][0]

    elif event == "Edit":
        try:
            todos = fn.get_todos()
            todos[todos_index] = value['todo'] + "\n"
            fn.write_todos("text.txt", todos)
            window['todos'].update(values=todos)
        except NameError:
            sg.popup("Please select an item to edit.")

    elif event == "Complete":
        try:
            todos = fn.get_todos()
            todos.remove(todo_value)
            fn.write_todos("text.txt", todos)
            window['todos'].update(values=todos)
        except NameError:
            sg.popup("Please select to do to complete.")
    elif event == "Exit":
        break
        
    elif event == sg.WIN_CLOSED:
        break

window.close()
