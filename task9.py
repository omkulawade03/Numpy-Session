# ==========================
# Q1. Creating Dictionaries
# ==========================

# (a) Empty dictionary - Method 1
dict1 = {}

# Empty dictionary - Method 2
dict2 = dict()

print("Empty Dictionary (Method 1):", dict1)
print("Type:", type(dict1))

print("Empty Dictionary (Method 2):", dict2)
print("Type:", type(dict2))


# (b) Dictionary with string keys
student = {
    "name": "Rahul",
    "city": "Pune",
    "course": "Python"
}

print("\nDictionary with String Keys:", student)
print("Type:", type(student))


# (c) Dictionary with integer keys
numbers = {
    1: "One",
    2: "Two",
    3: "Three"
}

print("\nDictionary with Integer Keys:", numbers)
print("Type:", type(numbers))


# (d) Mixed data type dictionary
mixed_dict = {
    "name": "Amit",   # string value
    "age": 21,        # integer value
    "cgpa": 8.75      # float value
}

print("\nMixed Data Type Dictionary:", mixed_dict)
print("Type:", type(mixed_dict))

# ==========================
# Q2. Accessing and Modifying Elements
# ==========================

# Creating a dictionary
student = {
    "name": "YourName",
    "age": 20,
    "city": "YourCity",
    "marks": 80
}

# Accessing value using square brackets
print("Name:", student["name"])

# Updating marks
student["marks"] = 92

# Adding a new key-value pair
student["grade"] = "A"

# Printing updated dictionary
print("\nUpdated Dictionary:")
print(student)

# ==========================
# Q3. get(), keys(), values(), items()
# ==========================

# Creating a dictionary
person = {
    "name": "Om Kulawade",
    "age": 21,
    "profession": "AIML"
}

# (a) Using get()
print("Age:", person.get("age"))
print("Salary:", person.get("salary", "Not Available"))

# (b) Printing all keys
print("\nKeys:")
print(person.keys())

# (c) Printing all values
print("\nValues:")
print(person.values())

# (d) Printing all key-value pairs
print("\nItems:")
print(person.items())

students = {
"s1": {"name": "Rahul", "age": 20, "marks": 88},
"s2": {"name": "Sneha", "age": 21, "marks": 95}
}

# ==========================
# Q4 (Nested Dictionary)
# ==========================
# Create a nested dictionary
students = {
    "student1": {
        "name": "OM KULAWADE",
        "age": 20,
        "marks": 85
    },
    "student2": {
        "name": "ATHARVA WAGH",
        "age": 21,
        "marks": 88
    }
}

# Print the details of the first student
print("First Student Details:")
print(students["student1"])

# Print the marks of the second student
print("Second Student Marks:")
print(students["student2"]["marks"])

# Add a new subject "math" with marks 90 for the first student
students["student1"]["math"] = 90

# Print the updated dictionary
print("Updated Dictionary:")
print(students)

# ==========================
# Q5. (update() and pop())
# ==========================
info = {
    "brand": "Samsung",
    "model": "A52",
    "price": 25000
}

# Update the dictionary
info.update({"color": "Black", "price": 24000})

# Remove "model" and store the removed value
removed_value = info.pop("model")

# Print the removed value
print("Removed value:", removed_value)

# Print the final dictionary
print("Final dictionary:", info)

# ==========================
# Q6. (popitem() and clear())
# ==========================
# Create a dictionary with 5 key-value pairs
student = {
    "name": "Rahul",
    "age": 20,
    "city": "Pune",
    "marks": 85,
    "grade": "A"
}

# pop() removes a specific key and returns its value.
# Example: student.pop("age")

# popitem() removes and returns the last inserted key-value pair as a tuple.
# Example: student.popitem()

# Use popitem() twice
removed_item1 = student.popitem()
print("First removed item:", removed_item1)

removed_item2 = student.popitem()
print("Second removed item:", removed_item2)

# Clear the entire dictionary
student.clear()

# Print the final dictionary
print("Final dictionary:", student)

# ==========================
# Q7. (copy() and setdefault())
# ==========================
# Create a dictionary
d = {"a": 1, "b": 2}

# Make a copy of the dictionary
d_copy = d.copy()

# Add key "c" with value 3 if it doesn't exist
d_copy.setdefault("c", 3)

# Use setdefault() on an existing key "a"
d_copy.setdefault("a", 100)  # Value will not change

# Print the original and copied dictionaries
print("Original Dictionary:", d)
print("Copied Dictionary:", d_copy)

# ==========================
# Q8 (fromkeys() and Membership)
# ==========================
# Create a dictionary with default value None
person = dict.fromkeys(["name", "age", "city"], None)

# Take user input
person["name"] = input("Enter name: ")
person["age"] = input("Enter age: ")
person["city"] = input("Enter city: ")

# Display the dictionary
print("\nDictionary:")
print(person)

# Check if a key exists
key = input("\nEnter a key to check: ")

if key in person:
    print(f"'{key}' exists in the dictionary.")
else:
    print(f"'{key}' does not exist in the dictionary.")

# ==========================
# Q9 (Practical Application)
# ==========================
# Dictionary to store contacts
contacts = {}

# Take input from user
name = input("Enter contact name: ")
phone = input("Enter phone number: ")
email = input("Enter email address: ")

# Store contact information
contacts[name] = {
    "phone": phone,
    "email": email
}

# Search for a contact
search_name = input("\nEnter name to search: ")

contact = contacts.get(search_name)

if contact:
    print("\nContact Found:")
    print("Phone:", contact["phone"])
    print("Email:", contact["email"])
else:
    print("Contact not found.")

# Print all contacts
print("\nAll Contacts:")
for name, details in contacts.items():
    print(f"Name: {name}")
    print(f"Phone: {details['phone']}")
    print(f"Email: {details['email']}")
    print("-" * 20)

# ==========================
# Q10. (Mini Project - Combined Concepts)
# ==========================
# Student Management System

# Dictionary to store student records
students = {}

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add New Student")
    print("2. Update Student Marks")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Remove Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add new student
    if choice == "1":
        roll_no = input("Enter Roll Number: ")

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        students[roll_no] = {
            "name": name,
            "age": age,
            "marks": marks
        }

        print("Student added successfully!")

    # Update marks
    elif choice == "2":
        roll_no = input("Enter Roll Number: ")

        if roll_no in students:
            new_marks = float(input("Enter New Marks: "))

            # Update marks using update()
            students[roll_no].update({"marks": new_marks})

            print("Marks updated successfully!")
        else:
            print("Student not found.")

    # Search student
    elif choice == "3":
        roll_no = input("Enter Roll Number: ")

        student = students.get(roll_no)

        if student:
            print("\nStudent Found:")
            print("Name :", student["name"])
            print("Age  :", student["age"])
            print("Marks:", student["marks"])
        else:
            print("Student not found.")

    # Display all students
    elif choice == "4":
        if not students:
            print("No student records available.")
        else:
            print("\nAll Students:")
            for roll_no, details in students.items():
                print(f"\nRoll No: {roll_no}")
                print(f"Name   : {details['name']}")
                print(f"Age    : {details['age']}")
                print(f"Marks  : {details['marks']}")

    # Remove a student
    elif choice == "5":
        roll_no = input("Enter Roll Number: ")

        removed_student = students.pop(roll_no, None)

        if removed_student:
            print("Student removed successfully!")
        else:
            print("Student not found.")

    # Exit program
    elif choice == "6":
        print("Exiting Student Management System...")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please try again.")









