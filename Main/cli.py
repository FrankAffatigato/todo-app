user_prompt = "Type add, show, edit, complete or exit: \n"

"""Define function to grab list of to-dos from text file"""
import function as fn
import time

time_now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"it is {time_now}")

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
    user_action = user_action.lower() 

        
    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:] + '\n'
        with open('text.txt', 'a') as file:
            file.write(todo)

    elif 'show' in user_action or 'display' in user_prompt:
        todos = fn.get_todos('text.txt')
        
        for item_num, item in enumerate(todos):
            item = item.title()
            item = item.strip('\n')
            print(f'{item_num + 1}. {item}')
    
    elif user_action.startswith('complete'):
        try:   
            todos = fn.get_todos('text.txt')
            
            complete_item = int(user_action[9:].strip()) - 1
            todos.pop(complete_item)
            
            #Write new list with item completed
            fn.write_todos('text.txt', todos)
        except IndexError:
            print('Your command is not valid')
            continue
        except ValueError:
            print('Your command is not valid')
            continue
    
    #Edit an item in the to-do list
    elif user_action.startswith('edit'):
    
        try:
            todos = fn.get_todos('text.txt')
        
            edit_input = int(user_action[5:].strip()) - 1
            new_item = input("Enter new task \n")
            todos[edit_input] = new_item + "\n"
        
        #Write the new edited list
            fn.write_todos('text.txt', todos)
        except ValueError:
            print('Your command is not valid')
            continue
    
    elif user_action.startswith('exit'):
        break
    else:
        print('Command not found')
print("Bye!")