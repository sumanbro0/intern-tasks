import json

def save(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def load(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

todos_filename = 'todos.json'
bin_filename = 'bin.json'

todos = load(todos_filename)
bin = load(bin_filename)

exit=False
help=True
while(not exit):
    if help==True:
            print(
        '''
        . add -> add a task to the to-do list.\n
        . complete -> mark a task as complete.\n
        . view all -> view the current tasks in the to-do list.\n
        . view complete -> view all the completed tasks in the to-do list.\n
        . delete -> Delete the to-do list and take it to the bin if it’s not\n
        . rmanent.\n
        . view incomplete -> view all the incomplete tasks in the to-do list.\n
        . view bin -> view all the tasks that are deleted and are not\n
          currently in bin.\n
        . restore -> restore the deleted task from the bin. \n
        . clear bin -> delete all the to-dos that are presented in the bin.\n
        . help -> display all the help message. \n
        . exit -> exit the program.\n

        '''
    )
    help=False
    command=str(input("Enter Command: ")).lower().strip()
    try:
        match command:
            case "add":
                task={"status":"incomplete"}
                desc=str(input("Enter Task: ")).lower().strip()
                task["desc"]=desc
                found=False
                for todo in todos:
                   if todo["desc"]==task["desc"]:
                       found=True
                if not found:
                    todos.append(task)
                    print("Task added")
                else:
                    print("Task already added")
                

            case 'complete':
                try:
                    comp=int(input("Enter Task number to complete: "))
                    completed=todos[comp-1]
                    if completed:
                        completed["status"]="complete"
                        print("Task Completed")
                except Exception as e:
                    print("Task id invalid",e)

                
            case "view all":
                if todos:
                    for i,todo in enumerate(todos):
                        print(f"\nsn:{i+1}\ndescription:{todo['desc']}\nStatus:{todo['status']}\n".center(100,"*"))
                else:
                    print("Empty todo list")

            case "view complete":
                if todos:
                    for i,todo in enumerate(todos):
                        if todo['status']=='complete':
                            print(f"\nsn:{i+1}\ndescription:{todo['desc']}\nStatus:{todo['status']}\n".center(100,"*"))
                        else:
                            print("No tasks completed")
                else:
                    print("Empty todo list")

            case "view incomplete":
                if todos:
                    for i,todo in enumerate(todos):
                        if todo['status']=='incomplete':

                            print(f"\nsn:{i+1}\ndescription:{todo['desc']}\nStatus:{todo['status']}\n".center(100,"*"))
                        else:
                            print("No tasks incomplete")
                else:
                    print("Empty todo list")

            case "help":
                help=True

            case "exit":
                print("Do You Really want to exit?")
                choice=str(input("Enter(yes/no): ")).lower().strip()
                if choice=="yes":
                    save(todos, todos_filename)
                    save(bin, bin_filename)
                    exit=True

            case "delete":
                task_id=int(input("Enter Task No. to be deleted: "))
                try:
                    to_be_deleted=todos[task_id-1]
                    print("Do You want to delete Permanently?\n")
                    choice=str(input("Enter(yes/no): ")).lower().strip()
                    if choice=="yes":
                        todos.remove(to_be_deleted)
                    elif choice=="no":
                        bin.append(to_be_deleted)
                        todos.remove(to_be_deleted)
                    else:
                        print("Invalid command")
                except Exception as e:
                    print(e)


            case "view bin":
                if bin:
                    for i,b in enumerate(bin):
                        print(f"\nsn:{i+1}\ndescription:{b['desc']}\nStatus:{b['status']}\n".center(100,"*"))
                else:
                    print("Empty bin")

            case "restore":
                if bin:
                    choice=int(input("Enter Task No. to be restored: "))
                    try:
                        task_to_restore=bin[choice-1]
                        todos.append(task_to_restore)
                        bin.remove(task_to_restore)
                    except Exception as e:
                        print(e)
                    
                else:
                    print("Empty bin")
            
            case "clear bin":
                if bin:
                    bin.clear()
                    print("Bin Cleared")
                else:
                    print("bin already empty ")
            
            case _:
                print("Invalid Option")
                help=True

    except Exception as e:
        print(e)
            
            
            



