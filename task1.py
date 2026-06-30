# ==========================
# Q1
# ==========================
full_name = "Om Prashant Kulawade"
age = 18
height_meters = 2.13
is_student = True

print("Full Name:", full_name)
print("Age:", age)
print("Height (meters):", height_meters)
print("Student:", is_student)

print("\nData Types:")
print(type(full_name))
print(type(age))
print(type(height_meters))
print(type(is_student))


# ==========================
# Q2
# ==========================
name = "Om Prashant Kulawade"
age = 18
height = 2.13
is_student = True

print("\nName:", name)
print("Data Type:", type(name))

print("Age:", age)
print("Data Type:", type(age))

print("Height:", height)
print("Data Type:", type(height))

print("Student:", is_student)
print("Data Type:", type(is_student))

age_float = float(age)
height_int = int(height)

print("\nAfter Conversion:")
print("age_float =", age_float)
print("Data Type:", type(age_float))

print("height_int =", height_int)
print("Data Type:", type(height_int))


# ==========================
# Q3
# ==========================
a = 15
b = 4

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulo:", a % b)
print("Exponentiation:", a ** b)


# ==========================
# Q4
# ==========================
x = 25
y = 30
z = 25

print("\nIs x greater than y?", x > y)
print("Is x equal to z?", x == z)
print("Is x less than or equal to y AND y is not equal to z?",
      (x <= y) and (y != z))
print("Is x greater than y OR x equal to z?",
      (x > y) or (x == z))


# ==========================
# Q5
# ==========================
name = input("\nEnter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = 2026
age = current_year - birth_year

print("\n----- User Details -----")
print(f"Name: {name}")
print(f"Age in {current_year}: {age} years")


# ==========================
# Q6
# ==========================
height = float(input("\nEnter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")


# ==========================
# Q7
# ==========================
length = float(input("\nEnter the length: "))
width = float(input("Enter the width: "))

area = length * width
perimeter = 2 * (length + width)

print("Area =", area)
print("Perimeter =", perimeter)


# ==========================
# Q8
# ==========================
fruits = ["mango", "apple", "banana", "cherry"]
score = 50

score += 25

apple_in_list = "apple" in fruits
grape_not_in_list = "grape" not in fruits

print("\nUpdated Score:", score)
print("Is 'apple' in the fruits list?", apple_in_list)
print("Is 'grape' not in the fruits list?", grape_not_in_list)


# ==========================
# Q9
# ==========================
student_name = input("\nEnter your name: ")
student_age = int(input("Enter your age: "))
student_city = input("Enter your city: ")

subject1_marks = float(input("Enter marks in Subject 1: "))
subject2_marks = float(input("Enter marks in Subject 2: "))
subject3_marks = float(input("Enter marks in Subject 3: "))

total_marks = subject1_marks + subject2_marks + subject3_marks
percentage = total_marks / 3

print("\n========== STUDENT PROFILE ==========")
print(f"Name       : {student_name}")
print(f"Age        : {student_age}")
print(f"City       : {student_city}")
print(f"Total Marks: {total_marks}")
print(f"Percentage : {percentage:.2f}%")
print("=====================================")


# ==========================
# Q10
# ==========================
name = "Alice"
age = 20
city = "Amsterdam"

print("\nMy name is " + name)
print("I am", age, "years old")
print("I live in", city)
print("Adult:", age > 18)