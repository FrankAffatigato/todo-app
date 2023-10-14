filepath = "text.txt"

def get_todos(filepath="text.txt"):
    with open(filepath, 'r') as todos_file:
                todos_local = todos_file.readlines()
    return todos_local

#Define function to write new list of to-dos back to text file
def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
                file.writelines(todos_arg)