import PySimpleGUI as sg
import zip_func as zf

input_label = sg.Text("Enter Input Filepath   ")
input_filepath = sg.InputText()
input_button = sg.FilesBrowse("Input")

output_label = sg.Text("Enter Output Filepath")
output_filepath = sg.InputText()
output_button = sg.FolderBrowse("Output")

compress_button = sg.Button("Compress")
window = sg.Window("File Compressor App", layout=[[input_label, input_filepath, input_button], 
                                                  [output_label, output_filepath, output_button], 
                                                  [compress_button]])


event, value = window.read()
print(event, value)
print(value)
input_path = value["Input"]
output_path = value["Output"] + "/text.zip"

print(input_path)
print(output_path)

zf.compress_file(input_path, output_path)

window.close()