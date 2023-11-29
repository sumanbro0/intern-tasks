import datetime

import report_generation
import book_management,member_management
book=book_management.Book
member=member_management.LibraryMember
class Transaction:
    trans=[]
    def __init__(self,taken_by,b):
        self.mem=taken_by
        self.b=b
        self.borrowed_date=datetime.datetime.now()
        self.return_date = datetime.datetime.now()+ datetime.timedelta(seconds=1)
        self.fine=0


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
            kitab=Transaction(mem,b)
            self.trans.append(kitab)
            print(self.trans)
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
t=Transaction(object,object)


class Reports:
    a=0
    def generate_log_file(self):
        log_filename = f"transaction_log{Reports.a}.txt"
        with open(log_filename, "w") as log_file:
            for i in t.trans:
                print(i.return_date<datetime.datetime.now(),datetime.datetime.now())
                if i.return_date < datetime.datetime.now():
                    extra_time = datetime.datetime.now()-i.return_date 
                    if extra_time > datetime.timedelta(minutes=1):
                        try:
                            i.fine = int(extra_time.total_seconds() // 60) * 5
                            log_file.write(f"Transaction ID: {i.mem.id}\n")
                            log_file.write(f"Return Date: {i.return_date}\n")
                            log_file.write(f"Fine: ${i.fine}\n")
                            log_file.write("\n")
                            Reports.a+=1
                        except Exception as e :
                            print(e)
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
        • fines\n
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
            case "fines":
                Reports().generate_log_file()

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