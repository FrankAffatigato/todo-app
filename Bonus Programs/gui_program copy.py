import PySimpleGUI as sg
import zip_creator as zc

input_label = sg.Text("Enter Input Filepath   ")
input_filepath = sg.InputText()
input_button = sg.FilesBrowse("Input", key="files")

output_label = sg.Text("Enter Output Filepath")
output_filepath = sg.InputText()
output_button = sg.FolderBrowse("Output", key="folder")

zipname_label = sg.Text("Name your compressed file")
zipname = sg.InputText(key="zipname")

compress_button = sg.Button("Compress")
output = sg.Text(key="output")

window = sg.Window("File Compressor App", layout=[[input_label, input_filepath, input_button], 
                                                  [output_label, output_filepath, output_button],
                                                  [zipname_label, zipname], 
                                                  [compress_button],
                                                  [output]])

while True:
    event, value = window.read()
    if event == "Compress":
        print(event, value)
        print(value)
        input_path = value["files"].split(";")
        output_path = value["folder"]
        filename = value["zipname"]

        print(input_path)
        print(output_path)

        zc.mark_archive(input_path, output_path, filename)
        window["output"].update(value="Compression completed!")

    elif event == sg.WIN_CLOSED:
            break

window.close()