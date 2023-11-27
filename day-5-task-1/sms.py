

class Student:
    students = []
    roll_no=0
    def __init__(self, name, marks):
        self.roll =Student.roll_no
        self.name = name
        self.marks = marks
        Student.roll_no+=1


    def __str__(self):
        return f"Students_name:{self.name}\nStudents_marks={self.marks}\nStudents_roll={self.roll}\n"

    def add_student(self):
        while True:
            try:
                name = str(input("Enter name:")).strip().lower()
                marks = int(input("Enter marks:"))
                student = Student(name, marks)
                print(f'\n{student}'.center(100,'*'))
                self.students.append(student)

                choice = str(input("Add more? (y/n): ")).lower().strip()
                if choice == 'n':
                    break
            except Exception as e:
                print(e)

    def view(self):
        if self.students:
            sorted_list = sorted(self.students, key=lambda x: x.marks)
            for s in sorted_list:
                print(f"\nname:{s.name}\nroll:{s.roll}\nmarks:{s.marks}\n".center(100, "*"))
        else:
            print("No students currently")

    def search(self):
        roll=int(input("Roll no: "))
        for student in self.students:
            if student.roll==roll:
                print(f"\nname:{student.name}\nroll:{student.roll}\nmarks:{student.marks}\n".center(100, "*"))
            else:
                print("Student doesnot exists")


    def update(self):
        roll=int(input("Roll no: "))
        self.found=False
        for student in self.students:
            if student.roll==roll:
                self.found=True
                name=str(input("Enter Name to update: "))
                marks=int(input("Enter Marks to update: "))
                if name:
                    student.name=name
                if marks:
                    student.marks=marks
        if not self.found:
            print("Student not found")

    def delete(self):
        roll=int(input("Roll no: "))
        self.found=False
        for student in self.students:
            if student.roll==roll:
                self.found=True
                self.students.remove(student)
        if not self.found:
            print("Student not found")
    

def show_help(show=False):
    if show:
        print(
        '''
        • add \n
        • view\n
        • search\n
        • update\n
        • delete\n
        • help\n
        • exit\n
        '''
        )



std = Student("s",0)

show_help(True)
try:
    while True:
        command=str(input("enter command: ")).strip().lower()
        match command:
            case "add":
                std.add_student()
            case 'view':
                std.view()
            case 'search':
                std.search()
            case 'update':
                std.update()
            case 'delete':
                std.delete()
            case 'help':
                show_help(True)
            case 'exit':
                print("Tata")
                break
            case _:
                print("Invalid command")
                show_help(True)



except Exception as e:
    print(e)