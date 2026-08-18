class Student:
    def __init__(self,name,register_no,department,marks):
        self.name=name
        self.register_no=register_no
        self.department=department
        self.marks=marks
    def totalmarks(self):
        return sum(self.marks) #returns the total mark which was secured by the Student
    def averagemarks(self):
        if(len(self.marks)==0):
            return 0
        else:
            ave=self.totalmarks()/len(self.marks) #returns the average mark secured by the Student
            return ave
    def numberofpassedsub(self):
        passcount=0
        for i in self.marks:
            if(i>=40):
                passcount+=1 #returns the number of passed subjects by the Student
        return passcount
    def result(self):
        return self.numberofpassedsub()==len(self.marks)
    def grade(self):
        ave=self.averagemarks()
        if(ave>=90):
            return "A"
        elif(ave>=80):
            return "B"
        elif(ave>=70):
            return "C"
        elif(ave>=60):
            return "D"
        elif(ave>=50):
            return "E"
        elif(ave>=40):
            return "F"
        else:
            return "G" 
    def display(self):
        print("NAME       :",self.name)
        print("REGISTER NO:",self.register_no)
        print("DEPARTMENT :",self.department)
        print("MARKS      :",self.marks)
        print("TOTAL MARKS:",self.totalmarks())
        print("AVERAGE    :",self.averagemarks())
        print("GRADE      :",self.grade())
        passed=self.numberofpassedsub()
        if passed==len(self.marks):
            print(f"Congratulations! You passed the exam... clearing all {passed} subjects")
        else:
            print(f"Sorry... Your marks does not satisfy the passing criteria...in {len(self.marks)-passed} subjects")
        print()
students=[]
def addstudents():
    n=int(input("Enter the number of students you want to add:"))
    for i in range(n):
        print("enter name:")
        name=input()
        print("enter reg number:")
        regno=input()
        print("enter department:")
        dept=input()
        print("enter marks:")
    while True:
        try:
            mark=list(map(int,input().split()))
            valid=1
            for m in mark:
                if(m<0 or m>100):
                    valid=0
                    break
            if valid:
                break
            else:
                print("Enter marks between 0 to 100...")
        except ValueError:
            print("Enter valid marks only...")
    student=Student(name,regno,dept,mark)
    inv_regno=0
    for i in students:
        if i.register_no==regno:
            inv_regno=1
            print("A student already exists with this register number...")
            break
    if inv_regno==0:
        students.append(student)
def displaystudents():
        for i in students:
            i.display()
def searchstudent():
        regno=input("enter the student register number you want to search:")
        found=0
        for i in students:
            if(i.register_no==regno):
                print("\nStudent Found!")
                i.display()
                found=1
                break
        if(found==0):
            print("\nStudent not found!")
def updatestudent():
        regno=input("enter the student register number of the student you want to modify...")
        found=0
        for i in students:
            if(i.register_no==regno):
                print("\nStudent Found!")
                i.display()
                found=1
                print("1.update name")
                print("2.update marks")
                print("3.update both")
                update=int(input("enter your updation choice..."))
                if(update==1):
                    name=input("Enter the new name:")
                    i.name=name
                elif(update==2):
                    while True:
                        try:
                            marks=list(map(int,input().split()))
                            valid=0
                            for j in marks:
                                if j<0 or j>100:
                                    print("enter only valid marks")
                                    valid=1
                                    break
                            if(valid==0):
                                i.marks=marks
                            else:
                                print("You entered invalid marks...hence marks will remain same")
                        except ValueError:
                            print("Enter only valid marks...")
                elif(update==3):
                    name=input("Enter the new name:")
                    i.name=name
                    marks=list(map(int,input().split()))
                    valid=0
                    for j in marks:
                        if j<0 or j>100:
                            print("enter only valid marks")
                            valid=1
                            break
                    if(valid==0):
                        i.marks=marks
                    else:
                        print("You entered invalid marks...hence only the name gets changed,marks will remain same")
                else:
                    print("Invalid choice")
                break
        if(found==0):
            print("\nStudent not found!")
def deletestudent():
        regno=input("enter the student register number of the student you want to delete:")
        found=0
        for i in students:
            if(i.register_no==regno):
                print("\nStudent Found!")
                i.display()
                students.remove(i)
                print("You have successfully deleted the student")
                found=1
                break
        if(found==0):
            print("\nStudent not found!")
def invalid():
        print("Invalid choice")
while True:
    print("=================================================================")
    print("WELCOME TO STUDENT MANAGEMENT SYSTEM")
    print("=================================================================")
    print("WHAT ARE YOU LOOKING FOR?")
    print("\n1.ADD STUDENT")
    print("2.DISPLAY STUDENTS")
    print("3.SEARCH STUDENT")
    print("4.UPDATE STUDENT")
    print("5.DELETE STUDENT")
    print("6.EXIT")
    try:
        choice=int(input("\nEnter your choice :"))
        if(choice==1):
            addstudents()
        elif(choice==2):
            displaystudents()
        elif(choice==3):
            searchstudent()
        elif(choice==4):
            updatestudent()
        elif(choice==5):
            deletestudent()
        elif(choice==6):
            print("THANKYOU FOR USING STUDENT MANAGEMENT SYSTEM...")
            break
        else:
            invalid()
    except ValueError:
        print("Enter only valid numbers...")
