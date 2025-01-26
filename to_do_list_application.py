# To Do List Application

to_do_list = [] #empty list
            
def add_task(): #created function to add tasks
    task = input("\nEnter the task you wish to add: ")
    if task == "":
        print("\nYou did not add a task, please try again!")
    else:
        to_do_list.append(task) #stores new tasks to the list
        print(f"\n'{task}' was added to the list.")

def view_task(): #created function to view the to do list
    if not to_do_list: # used if not condition to determine if anything is in the list
        print("\nThere are no tasks to view")
    else:
        print("\nTo do list: ")
        for index, task in enumerate(to_do_list): #decided to numerate the index to make the app user friendly
            print(f"Task #{index}. {task}") 
            
def delete_task():
    view_task() #add the view task function so the user can see the tasks to remove
    try: #used try and except to catch any invalid inputs/errors
        remove_task = int(input("\nEnter the number of the task you wish to delete: "))
        if remove_task >= 0 and remove_task < len(to_do_list): #used 'if and' to give an error when the task to be deleted exceeds the amount in the list
            to_do_list.pop(remove_task) #used to remove elements from the list
            print(f"\nTask #{remove_task}. has been deleted.")
        else:
            print(f"\nTask #{remove_task}. does not exist")
    except:
        print("\nInvalid input, please try again")
    
if __name__ == "__main__": #loop to run the app
    print("Welcome to the To Do List App!")
    while True:
        print("\nPlease make a selection from the menu: ")
        print("-" * 30)
        print("1. Add tasks")
        print("2. View tasks")
        print("3. Delete tasks")
        print("4. Quit Application")
        
        user_selection = input("Enter the number here: ")
        
        if user_selection == "1":
            add_task()
        elif user_selection == "2":
            view_task()
        elif user_selection == "3":
            delete_task()
        elif user_selection == "4":
            break
        else:
            print("\nInvalid option, please try again!")
    
