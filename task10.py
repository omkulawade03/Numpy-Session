# ==========================
# Q1. Basic Class and Object
# ==========================
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

# Creating objects
car1 = Car("Rolls-Royce", "Phantom")
car2 = Car("Rolls-Royce", "Ghost")

# Calling methods
car1.display_info()
print()
car2.display_info()

# ==========================
# Q2. Using init Constructor
# ==========================
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

# Creating book objects
book1 = Book("The Art of Baahubali", "S. S. Rajamouli", 1200)
book2 = Book("RRR: Behind the Scenes", "S. S. Rajamouli", 1500)

book1.show_details()
print()
book2.show_details()
# ==========================
# Q3. Instance Methods and self)
# ==========================
class BankAccount:
    # Constructor
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient balance!")

    # Show current balance
    def show_balance(self):
        print(f"Current Balance: ₹{self.balance}")


# Create an object
account1 = BankAccount("Rahul Sharma", 5000)

# Demonstrate methods
account1.show_balance()

account1.deposit(2000)
account1.show_balance()

account1.withdraw(3000)
account1.show_balance()

account1.withdraw(5000) 
account1.show_balance()
# ==========================
# Q4. Method with Parameters)
# ==========================
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"


# Creating 3 student objects
student1 = Student("Amit", 75)
student2 = Student("Priya", 38)
student3 = Student("Rahul", 50)

# Displaying details and grades
for student in [student1, student2, student3]:
    print("Name:", student.name)
    print("Marks:", student.marks)
    print("Grade:", student.calculate_grade())
    print("-" * 20)

# ==========================
# Q5. Multiple Methods)
# ==========================
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Employee Name:", self.name)
        print("Salary: ₹", self.salary)

    def give_raise(self, amount):
        self.salary += amount
        print("New Salary after raise: ₹", self.salary)

    def yearly_bonus(self):
        return self.salary * 0.10


# Creating an employee object
emp = Employee("Virat", 50000)

# Demonstrating all methods
emp.display_details()

emp.give_raise(5000)

bonus = emp.yearly_bonus()
print("Yearly Bonus: ₹", bonus)
# ==========================
# Q6. Real-world Object Modeling)
# ==========================
class MobilePhone:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage

    def charge(self, percent):
        self.battery_percentage += percent
        if self.battery_percentage > 100:
            self.battery_percentage = 100
        print(f"Charged by {percent}%. Battery: {self.battery_percentage}%")

    def use_phone(self, minutes):
        battery_used = minutes // 10  # 1% battery for every 10 minutes
        self.battery_percentage -= battery_used

        if self.battery_percentage < 0:
            self.battery_percentage = 0

        print(f"Used phone for {minutes} minutes. Battery: {self.battery_percentage}%")

    def show_status(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Battery Percentage:", self.battery_percentage, "%")


# Creating an object
phone = MobilePhone("Samsung", "Galaxy S24", 80)

# Showing initial status
phone.show_status()

# Simulating usage
phone.use_phone(30)     # Reduces battery by 3%
phone.show_status()

# Charging the phone
phone.charge(15)        # Increases battery by 15%
phone.show_status()

# More usage
phone.use_phone(50)     # Reduces battery by 5%
phone.show_status()
# ==========================
#Q7. Combining Concepts)
# ==========================
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())


# Taking input from user
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Creating Rectangle object
rect = Rectangle(length, width)

# Displaying results
rect.display()

# ==========================
#Q8. Updating Attributes)
# ==========================
class Player:
    def __init__(self, name, score, level):
        self.name = name
        self.score = score
        self.level = level

    def increase_score(self, points):
        self.score += points
        print(f"Score increased by {points}. Current Score: {self.score}")

    def level_up(self):
        self.level += 1
        print(f"Level Up! Current Level: {self.level}")

    def show_progress(self):
        print("\nPlayer Progress")
        print("Name:", self.name)
        print("Score:", self.score)
        print("Level:", self.level)


# Creating a Player object
player1 = Player("Om Kulawade", 100, 1)

# Showing initial progress
player1.show_progress()

# Updating score and level multiple times
player1.increase_score(50)
player1.level_up()

player1.increase_score(75)
player1.level_up()

player1.increase_score(25)

# Showing final progress
player1.show_progress()
# ==========================
#Q9. Debugging OOP Code)
# ==========================
# Define the Person class
class Person:
    # Fix 1: Add 'self' as the first parameter in __init__
    def __init__(self, name, age):
        # Fix 2: Use self.name and self.age to store values as object attributes
        self.name = name
        self.age = age

    # Fix 3: Add 'self' as the first parameter in the method
    def introduce(self):
        # Fix 4: Use self.name and self.age to access object attributes
        # Fix 5: Correct the print statement syntax using an f-string
        print(f"My name is {self.name} and I am {self.age} years old.")


# Create an object of the Person class
p1 = Person("Rahul", 25)

# Fix 6: Call the method with parentheses
p1.introduce()
# ==========================
#Q10. Mini Project - Combined OOP
# ==========================
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"

    def issue_book(self):
        if self.status == "Available":
            self.status = "Issued"
            print(f"Book '{self.title}' issued successfully.")
        else:
            print(f"Book '{self.title}' is already issued.")

    def return_book(self):
        if self.status == "Issued":
            self.status = "Available"
            print(f"Book '{self.title}' returned successfully.")
        else:
            print(f"Book '{self.title}' is already available.")

    def show_info(self):
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {self.status}")
        print("-" * 30)


# Create some initial books
library = [
    Book("The Alchemist", "Paulo Coelho"),
    Book("Wings of Fire", "A.P.J. Abdul Kalam")
]

while True:
    print("\n===== Library Management System =====")
    print("1. Add a New Book")
    print("2. Issue a Book")
    print("3. Return a Book")
    print("4. Show All Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.append(Book(title, author))
        print("Book added successfully!")

    elif choice == "2":
        title = input("Enter book title to issue: ")
        found = False

        for book in library:
            if book.title.lower() == title.lower():
                book.issue_book()
                found = True
                break

        if not found:
            print("Book not found!")

    elif choice == "3":
        title = input("Enter book title to return: ")
        found = False

        for book in library:
            if book.title.lower() == title.lower():
                book.return_book()
                found = True
                break

        if not found:
            print("Book not found!")

    elif choice == "4":
        print("\nLibrary Books:")
        for book in library:
            book.show_info()

    elif choice == "5":
        print("Exiting Library Management System...")
        break

    else:
        print("Invalid choice! Please try again.")












