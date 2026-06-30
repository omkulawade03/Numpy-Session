# ==========================
# Q1
# Lambda function example
# ==========================
square = lambda x: x * x

num = int(input("Enter a number: "))
print("Square =", square(num))

def square_def(x):
    return x * x

print("Square using def =", square_def(num))


# ==========================
# Q2
# Add three numbers using lambda
# ==========================
add_three = lambda a, b, c: a + b + c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Sum =", add_three(a, b, c))


# ==========================
# Q3
# For loop examples
# ==========================
print("Numbers from 1 to 25:")
for i in range(1, 26):
    print(i)

total = 0
for i in range(1, 21):
    total += i

print("Sum of numbers from 1 to 20 =", total)

print("Table of 5:")
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)


# ==========================
# Q4
# Sum positive numbers using while loop
# ==========================
total = 0

while True:
    num = int(input("Enter a positive number (0 or negative to stop): "))

    if num <= 0:
        break

    total += num

print("Total Sum =", total)


# ==========================
# Q5
# Math module functions
# ==========================
import math

num = float(input("Enter a number: "))

print("Square Root =", math.sqrt(num))

if num >= 0 and num.is_integer():
    print("Factorial =", math.factorial(int(num)))
else:
    print("Factorial is only defined for positive integers.")

print("Ceiling Value =", math.ceil(num))
print("Floor Value =", math.floor(num))


# ==========================
# Q6
# Random number generation
# ==========================
import random

print("5 Random Integers:")
for i in range(5):
    print(random.randint(1, 100))

print("Random Number (50 to 150):", random.randrange(50, 151))
print("Random Float (0 to 1):", random.random())


# ==========================
# Q7
# Different ways to import modules
# ==========================
import math
from math import sqrt
import math as m

print("2 raised to the power 4 =", math.pow(2, 4))
print("Square root of 25 =", sqrt(25))
print("Factorial of 5 =", m.factorial(5))

# ==========================
# Q8
#task4.1 and task4.2

# ==========================
# Q9
# User-defined functions
# ==========================
def greet(name):
    print("Hello", name + ", Welcome to Python Class!")

def calculate_power(base, exp):
    return base ** exp


# ==========================
# Q10
# Main function example
# ==========================
def greet():
    print("Welcome to Python Programming!")

if __name__ == "__main__":
    greet()
    print("This file is running directly.")

