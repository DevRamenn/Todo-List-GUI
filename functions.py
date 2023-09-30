def get_todo_list(filepath='todos.txt'):
    """ Read a text file and return the list from it """
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_todos(todo_arg, filepath='todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_arg)
