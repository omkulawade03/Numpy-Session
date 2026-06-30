# ==========================
# Q1. (Basic try-except)
# ==========================
    
# Handles invalid number input

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Division =", num1 / num2)
except ValueError:
    print("Invalid input! Please enter numbers only.")

# ==========================
#Q2. (Handling ZeroDivisionError)
# ==========================
# Handles division by zero and invalid input

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Division =", num1 / num2)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Invalid input! Please enter numbers only.")

# ==========================
#Q3. (Multiple except Blocks)
# ==========================
# Handles different exceptions separately

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Division =", num1 / num2)

    text = input("Enter a value to convert into integer: ")
    number = int(text)
    print("Converted Integer =", number)

except ValueError:
    print("ValueError: Invalid input.")
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")

# ==========================
#Q4. (Using else)
# ==========================
# Else runs if no exception occurs

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Division =", result)

except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Division performed successfully!")
# ==========================
#Q5. (Using finally)
# ==========================
# Finally always executes

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Division =", num1 / num2)

except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    # Runs whether error occurs or not
    print("Program execution completed.")

# ==========================
#Q6. (Combined try-except-else-finally)
# ==========================
# Uses all exception blocks

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Division =", result)

except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Division successful!")

finally:
    print("Thank you for using the program.")

# ==========================
#Q7. (Practical - Age Input)
# ==========================
# Raises error for negative age

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Your age is:", age)

except ValueError as e:
    print("Error:", e)

# ==========================
#Q8. (Multiple Exceptions in One Block)
# ==========================
# Handles multiple exceptions together

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result =", result)

except (ValueError, ZeroDivisionError):
    print("Error: Invalid input or division by zero.")
# ==========================
#Q9. (Debugging Exception Code)
# ==========================
# Corrected exception syntax

try:
    num = int(input(" Enter a number: "))
    result = 100 / num
    print("Result:", result)

except ValueError:
    # Handles invalid integer input
    print("Please enter a valid number.")

except ZeroDivisionError:
    # Handles division by zero
    print("Cannot divide by zero.")

except Exception:
    # Handles any other error
    print("Some error occurred.")

# ==========================
#Q10. (Mini Project - Exception Handling)
# ==========================
# Simple calculator with exception handling

while True:

    print("\n===== Calculator Menu =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Exiting Calculator...")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result =", num1 + num2)

        elif choice == "2":
            print("Result =", num1 - num2)

        elif choice == "3":
            print("Result =", num1 * num2)

        elif choice == "4":
            print("Result =", num1 / num2)

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input! Enter numbers only.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    finally:
        print("Operation attempted.")



        
