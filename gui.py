import functions
import PySimpleGUI as gui

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo")
add_button = gui.Button("Add")

window = gui.Window('To-Do App by Ramen v1.0.0', layout=[[label], [input_box, add_button]])
window.read()
window.close()
