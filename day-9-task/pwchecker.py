import re
class Users:
    users=[]
    sn=0
    pattern="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    def __init__(self,name,email,password):
        self.id=Users.sn
        self.name=name
        self.email=email
        self.password=password
        Users.sn+=1

    def validate_password(self,password):
            return re.match(self.pattern,password)
            

    def add_user(self):
        name=str(input("Enter your name:")).strip()
        email=str(input("Enter your email:")).strip()
        password=str(input("Enter your password:")).strip()
        found=False
        if self.email and email in [mail.email for mail in self.users]:
            found=True
        if not found : 
            m=self.validate_password(password)
            if m:
                user=Users(name,email,password)
                self.users.append(user)
                print("done..")
            else:
                print("Sorry your password is weak")


u=Users("","","")
while True:
    command=str(input("Enter your choice (add,view,exit):")).strip().lower()
    match command:
            case "add":
                u.add_user()
            case "view":
                if u.users:
                    for i in u.users:
                        print(f'''
                            name:{i.name}\n
                            email:{i.email}\n
                            password:{i.password}\n
                        ''')
            case "exit":
                break
               


