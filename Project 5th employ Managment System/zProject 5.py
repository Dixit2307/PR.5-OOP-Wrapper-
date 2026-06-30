# Employee Management Sysetam

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Type: Person Created With  Name: {self.name}  Age: {self.age}.")



class Employee:
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary

    def display_details(self):
        print(f"Type: Employee Created With Name: {self.name} Age: {self.age} ID: {self.id} And Salary: {self.salary}. ")


class Manager:
    def __init__(self, name, age, id, salary,department):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary
        self.department = department

    def display_details(self):
        print(f"Type: Manager Created With Name: {self.name} Age: {self.age} ID: {self.id}  Salary: {self.salary} and Department {self.department} ")


    
# MAIN MENU 
while True:
    print("\n=== Python OOP Project : Employee Management System ===")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Showe Details")
    print("5. Exit")
   
   
    choice = input("Please enter your choice (1-5): ")
    
    if choice == "1":
        name = input("Enter person Name:")
        age = input("Enter Person's Age:")
        person = Person(name, age)
        person.display_details()

    elif choice == "2":
        name = input("Enter Employee Name :")
        age = input("Enter Employee Age :")
        id = input("Enter Emloyee ID :")
        salary = input("Enter Employee Salary :")
        e1 = Employee(name, age, id, salary)

        e1.display_details()

    elif choice == "3":
        name = input("Enter Manager Name :")
        age = input("Enter Manager Age :")
        id = input("Enter Manager ID :")
        salary = input("Enter Manager Salary :")
        department = input("Enter Department:")
        m1 = Manager(name, age, id, salary, department)
        m1.display_details()

    elif choice == "4":
        while True:
            print("\n chosse your Option") 
            print("1. Person")
            print("2. Employee")
            print("3. Manager")

            choice1= input("Please enter your choice (1-3): ")

            if choice1 == "1":
                person.display_details()
            elif choice1 == "2":
                e1.display_details()
            elif choice1 == "3":
                m1.display_details()
            else:
                print("Invalide Choise")
                break
        
    elif choice == "5":
        print("\nExiting the system ")
        break
    else:
        print("\nInvalid choice! Please try again.")
      


