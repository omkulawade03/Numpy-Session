# ==========================
# Q1: Voting Eligibility
# ==========================
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# ==========================
# Q2: Even or Odd
# ==========================
num = int(input("\nEnter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# ==========================
# Q3: Grade Calculator
# ==========================
marks = int(input("\nEnter marks: "))

if marks >= 90:
    print("Grade A - Excellent")
elif marks >= 75:
    print("Grade B - Good")
elif marks >= 60:
    print("Grade C - Average")
elif marks >= 40:
    print("Grade D - Pass")
else:
    print("Fail")

# ==========================
# Q4(a): Print 1 to 30
# ==========================
print("\nNumbers from 1 to 30:")
for i in range(1, 31):
    print(i)

# ==========================
# Q4(b): Odd Numbers 1 to 50
# ==========================
print("\nOdd Numbers from 1 to 50:")
for i in range(1, 51, 2):
    print(i)

# ==========================
# Q4(c): Sum of 1 to 15
# ==========================
total = 0

for i in range(1, 16):
    total += i

print("\nSum =", total)

# ==========================
# Q5: Number and Cube
# ==========================
print("\nNumbers and Cubes:")
num = 1

while num <= 20:
    print(num, "Cube =", num ** 3)
    num += 1

# ==========================
# Q6: Sum Until Negative or Zero
# ==========================
print("\nEnter positive numbers (0 or negative to stop):")
total = 0

while True:
    num = int(input("Enter a positive number: "))

    if num <= 0:
        break

    total += num

print("Total Sum =", total)

# ==========================
# Q7: Weather Checker
# ==========================
temperature = int(input("\nEnter temperature: "))
is_raining = input("Is it raining? (yes/no): ").lower()

if temperature > 30:
    if is_raining == "yes":
        print("Hot and rainy, carry umbrella.")
    else:
        print("Hot day, wear light clothes.")
elif temperature < 15:
    if is_raining == "yes":
        print("Cold and rainy, wear jacket and take umbrella.")
    else:
        print("Cold day, wear warm clothes.")
else:
    print("Weather is pleasant.")

# ==========================
# Q8: FizzBuzz
# ==========================
print("\nFizzBuzz from 1 to 40:")

for i in range(1, 41):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# ==========================
# Q9: Simple Calculator
# ==========================
while True:

    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting Calculator...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", num1 + num2)

    elif choice == 2:
        print("Result =", num1 - num2)

    elif choice == 3:
        print("Result =", num1 * num2)

    elif choice == 4:
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Result =", num1 / num2)

    else:
        print("Invalid choice")

# ==========================
# Additional Question 1
# ==========================
num = int(input("\nEnter a number: "))

if num > 100:
    print("Large number")
elif num > 50:
    print("Medium number")
else:
    print("Small number")

# ==========================
# Additional Question 2
# ==========================
print("\nCounting from 1 to 9:")

count = 1

while count < 10:
    print(count)
    count += 1