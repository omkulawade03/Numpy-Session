# ==========================
# Q1
# Basic Function
# ==========================
def welcome():
    print("Welcome to Python Programming!")

welcome()


# ==========================
# Q2
# Function with Parameter
# ==========================
def greet(name):
    print("Hello,", name + "! Welcome back")

greet("Krish")
greet("Shree")


# ==========================
# Q3
# Default Parameter
# ==========================
def show_message(message="Hello"):
    print(message)

show_message()
show_message("Good Morning")


# ==========================
# Q4
# Function with Return Value
# ==========================
def calculate_sum(a, b):
    return a + b

result = calculate_sum(10, 20)
print("Sum =", result)

def demo_print(a, b):
    print(a + b)

demo_print(5, 5)


# ==========================
# Q5
# Positional and Keyword Arguments
# ==========================
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info("Krish", 19)
student_info(age=19, name="Krish")


# ==========================
# Q6
# Square and Cube Function
# ==========================
def square(num):
    return num * num

def cube(num):
    return num * num * num

num = int(input("Enter a number: "))
print("Square =", square(num))
print("Cube =", cube(num))


# ==========================
# Q7
# Recursion - Countdown
# ==========================
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(10)


# ==========================
# Q8
# Recursion - Factorial
# ==========================
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))


# ==========================
# Q9
# Global and Local Variables
# ==========================
total = 0

def add_value(x):
    global total
    total += x
    print("Total =", total)

add_value(10)
add_value(20)
add_value(30)

def test():
    local_var = 100
    print(local_var)

test()


# ==========================
# Q10
# Simple Number Analyzer
# ==========================
def get_number():
    return int(input("Enter a Number (0 to exit): "))

def is_even(num):
    return num % 2 == 0

def power(base, exp=2):
    return base ** exp

def show_result(num):
    if is_even(num):
        print("Even Number")
    else:
        print("Odd Number")
    print("Square =", power(num))

while True:
    num = get_number()
    if num == 0:
        print("Program Ended")
        break
    show_result(num)