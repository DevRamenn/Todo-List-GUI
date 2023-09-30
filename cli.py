from functions import get_todo_list, write_todos
import time

print("Welcome to Todo List Creator v1.0 by Ramen")
time = time.strftime("It's %d-%b-%Y, %H:%M:%p")
print(time)
msg = "Type add, show, edit, delete or exit: "

while True:
    user_input = input(msg).strip().lower()

    if user_input.startswith('add'):
        todo = user_input[4:] + "\n"

        if user_input == 'add':
            todo = input("Type New TODO: ") + "\n"

        todo_list = get_todo_list('todos.txt')

        todo_list.append(todo)

        write_todos(todo_list)

        print(f"'{todo.strip()}' has been added successfully!")

    elif user_input.startswith('show'):
        todo_list = get_todo_list()

        # Method one to remove space or "\n"
        #
        # new_todo = [item.strip('\n') for item in todo_list]
        #
        # Method two to remove space below..
        #
        # new_todo = []
        # for item in todo_list:
        #     new_item = item.strip('\n')
        #     new_todo.append(new_item)
        print("Your All Todo Lists Below:")
        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            raw = f"{index + 1} - {item}"
            print(raw)

    elif user_input.startswith('edit'):
        try:
            todo_list = get_todo_list()

            if user_input == "edit":
                number = int(input("Number of the todo you want's to edit: "))

            else:
                number = int(user_input[5:])

            number -= 1

            old_todo = todo_list[number].strip()

            edit_input = input(
                f"Over-writing '{todo_list[number].strip()}' from the list, Please Type new todo: ") + "\n"
            todo_list[number] = edit_input

            write_todos(todo_list)

            print(f"'{old_todo}' replaced with '{edit_input.strip()}'! ")
        except ValueError:
            print("Your command is not valid!")
            continue

        except IndexError:
            print("Sorry! Your Input is out of range..")

            continue

    elif user_input.startswith('delete'):
        try:
            if user_input == "delete":
                number = int(input("Number of the todo you want's to delete: "))

            else:
                number = int(user_input[7:])

            todo_list = get_todo_list()

            removing_todo = todo_list[number - 1].strip()
            todo_list.pop(number - 1)

            write_todos(todo_list)

            massage = f"'{removing_todo}' successfully removed from your Todo list."
            print(massage)

        except ValueError:
            print("Your command is not valid!")
            continue
        except IndexError:
            print("Your command is not valid!")
            continue

    elif 'exit' in user_input:
        break

    else:
        print("Comment not found!")

print("bye")
