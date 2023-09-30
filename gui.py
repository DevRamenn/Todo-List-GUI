import functions
import PySimpleGUI as gui

label = gui.Text("Type in a To-Do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button("Add")

window = gui.Window('To-Do App by Ramen v1.0.0',
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todo_list()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case gui.WIN_CLOSED:
            break
        case "Edit":
            todos = functions.get_todo_list()
            print(todos)
        case "Delete":
            todos = functions.get_todo_list()



window.close()
