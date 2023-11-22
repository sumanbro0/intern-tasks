'''
3. Develop a Python program for managing books in a library with the following
functionalities:
3.1 Book Inventory: Initialise an empty list to represent the library's book
inventory.
3.2 Help Message: Display a help message to the user explaining the available
commands:
add -> add a book to the inventory
remove -> remove a book from the inventory
display -> display the current books in the inventory
exit -> exit the program
3.3 Book Addition: Implement the ability to add a book to the inventory. When
the user enters the add command, prompt them to enter the book title and
author. Ensure that the same book cannot be added twice.
3.4 Book Removal: Implement the ability to remove a book from the
inventory. When the user enters the remove command, prompt them to enter
the title of the book they want to remove. Display an appropriate message if
the book is not found in the inventory.
3.5 Inventory Display: Implement the display command to show the current
books in the inventory. Display a message if the inventory is empty.
3.6 Exit Confirmation: When the user enters exit, prompt them with "Are you
sure you want to exit?" If the user inputs "yes," the program should stop. If the
user inputs anything else, the program should continue.
'''

books=[]
exit=False
while(not exit):
    print(
        '''
        add -> add a book to the inventory\n
        remove -> remove a book from the inventory\n
        display -> display the current books in the inventory\n
        exit -> exit the program\n
        '''
    )
    command=str(input("Enter Command: ")).lower()
    try:
        match command:
            case "add":
                book={}
                book["title"]=str(input("Enter book title")).strip().lower()
                book["author"]=str(input("Enter book author")).strip().lower()
                if book not in books:
                    books.append(book)
                else:
                    print("Book already exists")
                

            case 'remove':
                book=str(input("Enter Book name to remove")).strip().lower()
                found=False
                for i,b in enumerate(books):
                    if b["title"]==book:
                        del books[i]
                        found=True
                        break
                if not found:
                    print("Book Not Found in library")
                
            case "display":
                if books:
                    print(books)
                else:
                    print("Books not found")


            case "exit":
                exit=True

    except Exception as e:
        print(e)
            
            
            



