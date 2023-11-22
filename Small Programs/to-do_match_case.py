user_prompt = "Type add, show, edit, complete or exit: \n"

#todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
    user_action = user_action.lower()  
    match user_action:
        
        case 'add':
            todo = input("Enter a todo: ") + '\n'
            with open('text.txt', 'a') as file:
              file.write(todo)

        case 'show' | 'display':
            with open('text.txt', 'r') as todos_file:
                todos = todos_file.readlines()
            
            for item_num, item in enumerate(todos):
                item = item.title()
                item = item.strip('\n')
                print(f'{item_num + 1}. {item}')
        
        case 'complete':
            with open('text.txt', 'r') as todos_file:
                todos = todos_file.readlines()
            
            for i, j in enumerate(todos):
                print(f'{i + 1}. {j}')
            complete_item = int(input('Enter the number of the item you completed.')) - 1
            todos.pop(complete_item)
        
        #Edit an item in the to-do list
        case 'edit':
            with open('text.txt', 'r') as todos_file:
                todos = todos_file.readlines()
            
            edit_input = int(input('What task number would you like to edit? \n')) -1
            new_item = input("Enter new task \n")
            todos[edit_input] = new_item
        case 'exit':
            break
print("Bye!")
