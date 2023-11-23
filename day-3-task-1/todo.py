todos=[]
exit=False
help=True
while(not exit):
    if help==True:
            print(
        '''
        • add -> add a task to the to-do list.\n
        • complete -> mark a task as complete.\n
        • view all -> view the current tasks in the to-do list.\n
        • view complete -> view all the completed tasks in the to-do list.\n
        • view incomplete -> view all the incomplete tasks in the to-do list.\n
        • help -> display all the help message.\n
        • exit -> exit the program.\n

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
                        print(f"sn:{i+1}\ndescription:{todo['desc']}\nStatus:{todo['status']}\n")
                else:
                    print("Empty todo list")

            case "view complete":
                if todos:
                    for i,todo in enumerate(todos):
                        if todo['status']=='complete':
                            print(f"sn:{i+1}\ndescription:{todo['desc']}\nStatus:{todo['status']}\n")
                        else:
                            print("No tasks completed")
                else:
                    print("Empty todo list")

            case "view incomplete":
                if todos:
                    for i,todo in enumerate(todos):
                        if todo['status']=='incomplete':

                            print(f"sn:{i+1}\ndescription:{todo['desc']}\nStatus:{todo['status']}\n")
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
                    exit=True
            
            case _:
                print("Invalid Option")
                help=True

    except Exception as e:
        print(e)
            
            
            



