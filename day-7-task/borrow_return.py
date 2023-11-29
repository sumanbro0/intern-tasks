import book_management,member_management
book=book_management.Book
member=member_management.LibraryMember
class Transaction:
    def __str__(self):
        print("take your required books")

    def borrow(self):
        member.show_members()
        id=int(input("Enter your user symbool no. (sn):"))
        mem=member.members[id-1]
        book.show()
        sn=int(input("Enter sn of book you want:"))
        b=[*book.books.values()][sn-1]
        if b.quantity>0 and mem.borrowed<5:
            b.quantity-=1
            mem.borrowed+=1
            mem.books.append(b)
        else:
            print("please return books to take other")


    def show_book(self):
        member.show_members()
        try:
            id=int(input("Enter your user symbool no. (sn):"))
            mem=member.members[id-1]
        except:
            print("INvalid sn")
        bks=mem.books
        
        book.display_books(bks,False)

    def return_book(self):
        member.show_members()
        try:
            id=int(input("Enter your user symbool no. (sn):"))
            mem=member.members[id-1]
        except:
            print("INvalid user sn")
        bks=mem.books
        book.display_books(bks,False)
        try:
            sn=int(input("Enter sn of book you want to return:"))
            b=bks[sn-1]
        except:
            print("INvalid book sn")
        
        if b:
            mem.borrowed-=1
            b.quantity+=1
            bks.pop(sn-1)
            print("Book returned successfully")
        else:
            print("invalid books serial no:")


t=Transaction()
def show_help(show=False):
    if show:
        print(
        '''
        • add books\n
        • show books\n
        • remove books\n
        • update books\n
        • add mem\n
        • show mem\n
        • remove mem\n
        • update mem\n
        • take books\n
        • return books\n
        • show my books\n
        • help\n
        • exit\n
        '''
        )
show_help(True)
try:
    while True:
        command=str(input("enter command: ")).strip().lower()
        match command:
            case "add books":    
                book.add()
            case "remove books":
                book.remove()
            case "show books":
                book.show()
            case "update books":
                book.update()
            case "add mem":    
                member.add_member()
            case "remove mem":
                member.remove_members()
            case "show mem":
                member.show_members()
            case "update mem":
                member.update_members()
            case "take books":
                t.borrow()
            case "return books":
                t.return_book()
            case "show my books":
                t.show_book()
            
            case "help":
                show_help(True)
            
            case "exit":
                print("Exitting...")
                break

            case _:
                print("Invalid command")
                show_help(True)
except Exception as e:
    print(e)