# ==========================
#Q1. Github Account Setup
# ==========================









'''# ==========================
#Q2. (Strings + Loops + Functions)
# ==========================
def analyze_string(s):
    # Check empty string
    if not s:
        print("String is empty")
        return

    # Print length
    print("Length:", len(s))

    # Print reverse string
    print("Reverse:", s[::-1])

    # Count vowels
    vowels = "aeiou"
    count = 0

    for ch in s.lower():
        if ch in vowels:
            count += 1

    print("Vowel Count:", count)

    # Print indexes
    print("\nCharacter Positions:")
    for i in range(len(s)):
        print(f"{s[i]} -> Positive Index: {i}, Negative Index: {i-len(s)}")


text = input("Enter a string: ")
analyze_string(text)

# ==========================
#Q3.Lists + Functions + Exception Handling
# ==========================
def manage_marks():
    marks = []

    print("Enter 5 subject marks")

    while len(marks) < 5:
        try:
            mark = float(input(f"Subject {len(marks)+1}: "))
            marks.append(mark)
        except ValueError:
            print("Please enter numbers only")

    average = sum(marks) / len(marks)

    print("Average:", average)
    print("Highest:", max(marks))
    print("Lowest:", min(marks))

    marks.sort(reverse=True)

    print("Marks in Descending Order:", marks)


manage_marks()

# ==========================
#Q4.OOP + Lists + Exception Handling
# ==========================
class Student:

    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    # Add mark
    def add_mark(self, mark):
        try:
            mark = float(mark)

            if 0 <= mark <= 100:
                self.marks_list.append(mark)
            else:
                print("Mark should be between 0 and 100")

        except ValueError:
            print("Invalid mark")

    # Calculate average
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0

        return sum(self.marks_list) / len(self.marks_list)

    # Display details
    def display_info(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks_list)
        print("Average:", self.get_average())


name = input("Enter student name: ")
roll = input("Enter roll number: ")

student = Student(name, roll)

for i in range(5):
    mark = input(f"Enter mark {i+1}: ")
    student.add_mark(mark)

student.display_info()

# ==========================
#Q5.Dictionaries + Functions + Control Structures
# ==========================
def student_database():
    students = {}

    while True:
        print("\n1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                roll = input("Roll Number: ")
                name = input("Name: ")
                age = int(input("Age: "))
                city = input("City: ")

                students.update({
                    roll: {
                        "name": name,
                        "age": age,
                        "city": city
                    }
                })

                print("Student Added")

            except ValueError:
                print("Invalid age")

        elif choice == "2":
            roll = input("Enter Roll Number: ")

            data = students.get(roll)

            if data:
                print(data)
            else:
                print("Student Not Found")

        elif choice == "3":
            if not students:
                print("No Records Found")
            else:
                for roll, data in students.items():
                    print("Roll:", roll)
                    print("Details:", data)

        elif choice == "4":
            print("Program Ended")
            break

        else:
            print("Invalid Choice")


student_database()

# ==========================
#Q6.Sets + Tuples + Modules
# ==========================
import random
import math

try:
    numbers = set()

    print("Enter 10 numbers")

    for i in range(10):
        num = int(input(f"Number {i+1}: "))
        numbers.add(num)

    num_tuple = tuple(numbers)

    print("Tuple:", num_tuple)

    if len(num_tuple) >= 3:
        print("Random Numbers:", random.sample(num_tuple, 3))
    else:
        print("Not enough unique numbers")

    total = sum(num_tuple)

    print("Square Root of Sum:", math.sqrt(total))

except ValueError:
    print("Invalid Input")

except Exception as e:
    print("Error:", e)

# ==========================
#Q7.Lambda + range() + Lists + Exception Handling
# ==========================
try:
    square = lambda x: x * x

    numbers = range(1, 21)

    squares = list(map(square, numbers))

    even_squares = [num for num in squares if num % 2 == 0]

    print("Even Squares:")
    print(even_squares)

except Exception as e:
    print("Error:", e)

# ==========================
#Q8.Tuples + Dictionaries + OOP
# ==========================
class Employee:

    # Constructor
    def __init__(self, emp_id, name, details):
        self.emp_id = emp_id
        self.name = name
        self.details = details

    # Show details
    def show_details(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])
        print()


employees = {}

employees[101] = Employee(101, "Om Kulawade", ("IT", 50000))
employees[102] = Employee(102, "Krish Dalvi", ("HR", 45000))
employees[103] = Employee(103, "Aditya Kumbhar", ("Sales", 40000))

for emp in employees.values():
    emp.show_details()

# ==========================
#Q9.Strings + Sets + Exception Handling + Modules
# ==========================
import math

try:
    sentence = input("Enter a sentence: ")

    words = sentence.split()

    unique_words = set(words)

    sorted_words = sorted(unique_words)

    print("Unique Words:")
    for word in sorted_words:
        print(word)

    count = len(unique_words)

    print("Unique Words Squared:", math.pow(count, 2))

except Exception as e:
    print("Error:", e)

# ==========================
#Q10.Mini Project - Smart Calculator & Data Manager
# ==========================
import math
import random
from datetime import datetime

history = {}


# Basic arithmetic
def basic_arithmetic():
    try:
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))

        op = input("Enter Operator (+,-,*,/): ")

        if op == "+":
            result = a + b

        elif op == "-":
            result = a - b

        elif op == "*":
            result = a * b

        elif op == "/":
            result = a / b

        else:
            print("Invalid Operator")
            return

        print("Result:", result)
        save_result(result)

    except Exception as e:
        print("Error:", e)


# Scientific calculations
def scientific_calculation():
    try:
        num = float(input("Enter Number: "))

        print("Square Root:", math.sqrt(num))
        print("Power 2:", math.pow(num, 2))
        print("Factorial:", math.factorial(int(num)))

    except Exception as e:
        print("Error:", e)


# Random numbers
def random_numbers():
    nums = [random.randint(1, 100) for i in range(5)]

    print("Random Numbers:", nums)

    save_result(nums)


# Store result
def save_result(result):
    time = str(datetime.now())

    history[time] = result


# View history
def view_history():
    if not history:
        print("No History Available")

    else:
        for time, result in history.items():
            print(time, "->", result)


# Main menu
while True:

    print("\n===== Smart Calculator =====")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Numbers")
    print("4. View History")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        basic_arithmetic()

    elif choice == "2":
        scientific_calculation()

    elif choice == "3":
        random_numbers()

    elif choice == "4":
        view_history()

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")'''