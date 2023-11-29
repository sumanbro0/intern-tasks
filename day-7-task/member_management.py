import datetime
import uuid


class LibraryMember:
    members=[]
    def __init__(self,name,address,dob):
        self.id=uuid.uuid4()
        self.name=name
        self.address=address
        self.dob=datetime.datetime.strptime(dob, '%Y-%m-%d')
        self.borrowed=0
        self.books=[]

    def display(mems):
        for i,m in enumerate(mems):
            print(f'''
                sn:{i+1}\n
                id:{m.id}\n
                Name:{m.name}\n
                Address:{m.address}\n
                Borrowed_books:{m.borrowed}\n
                Date of birth:{m.dob}\n
                Books:{m.books}
        '''.center(300,"*"))


    @classmethod
    def add_member(cls):
        name=str(input("Enter your name:")).strip()
        address=str(input("Enter address:")).strip()
        dob=str(input("Enter date of birth(yyyy-mm-dd): "))
        mem=LibraryMember(name,address,dob)
        cls.members.append(mem)

    @classmethod
    def show_members(cls):
        if cls.members:
            cls.display(cls.members)
        else: print("No members")

    @classmethod
    def update_members(cls):
        if cls.members:
            try:
                sn=int(input("Enter members symbool no.(sn): "))
                mem=cls.members[sn-1]
            except Exception as e:
                print(e)
            name=str(input("Enter name to be updated: ")).strip()
            address=str(input("Enter address to be updated: ")).strip()
            dob=str(input("Enter dob to be updated(yyyy-mm-dd): ")).strip()
            if name:
                mem.name=name
            if address:
                mem.address=address
            if dob:
                mem.dob=dob
        else:
            print("No members currently")

    @classmethod
    def remove_members(cls):
        if cls.members:
            cls.show_members()
            try:
                sn=int(input("Enter members symbool no.(sn): "))
            except Exception as e:
                print(e)
            if cls.members[sn-1] :
                cls.members.pop(sn-1)
            else: print("Members not found")
        else: print("No members")



