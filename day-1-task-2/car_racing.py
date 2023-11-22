states=["start","stop","exit"]
exit=False
state=states[1]
while(not exit):
    print("Available Commands")
    print("start -> start the car")
    print("stop -> stop the car")
    print("exit -> exit the program")
    print("What do you want?")
    command=str(input("Enter command: ")).lower()
    match command:
        case "start":
            if state is not states[0]:
                state=states[0]
                print("Car Started")
            else:
                print("Car is already Started")
        case "stop":
            if state is not states[1]:
                state=states[1]
                print("Car Stopped")
            else:
                print("Car is already Stopped")
        case "exit":
            print("Do You Really want to exit?")
            choice=str(input("Enter(yes/no): ")).lower()
            if choice=="yes":
                exit=True


