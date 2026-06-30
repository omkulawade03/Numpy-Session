# ==========================
# Q1. Creating Tuples
# ==========================

# Tuple with 5 numbers
t1 = (10, 20, 30, 40, 50)

# Mixed tuple
t2 = (100, "Python", 99.5, True)

# Empty tuples
t3 = ()
t4 = tuple()

# Single-element tuple
# Comma is required for a single-element tuple
t5 = (99,)

print("t1 =", t1, type(t1))
print("t2 =", t2, type(t2))
print("t3 =", t3, type(t3))
print("t4 =", t4, type(t4))
print("t5 =", t5, type(t5))


# ==========================
# Q2. Tuple Packing
# ==========================

# Tuple packing
person = "OM", 19, "Pune"

print("Tuple:", person)
print("Type:", type(person))

# Tuple unpacking
name, age, city = person

print("Name:", name)
print("Age:", age)
print("City:", city)

# ==========================
# Q3. Indexing and Negative Indexing
# ==========================

colors = ('red', 'green', 'blue', 'yellow', 'purple', 'orange')

print("First element:", colors[0])
print("Third element:", colors[2])
print("Last element:", colors[-1])
print("Second last element:", colors[-2])

index = int(input("Enter an index: "))

print("Element at index", index, ":", colors[index])

# ==========================
# Q4. Slicing Tuples
# ==========================

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Slicing syntax: tuple[start:end:step]
# start -> starting index (included)
# end -> ending index (excluded)
# step -> interval between elements

print("a) Elements from index 2 to 7:", numbers[2:8])
print("b) First 5 elements:", numbers[:5])
print("c) Last 4 elements:", numbers[-4:])
print("d) Every second element:", numbers[::2])
print("e) Reverse order:", numbers[::-1])

# ==========================
# Q5. Nested Tuples
# ==========================

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("First row:", matrix[0])
print("Second row, third column:", matrix[1][2])
print("Third row, first column:", matrix[2][0])

# ==========================
# Q6. Iterating and Unpacking
# ==========================

student = ('OM', 20, 'AIML', 'A')

# Iterate through the tuple
for item in student:
    print(item)

# Unpack the tuple
name, age, branch, grade = student

print("\nName:", name)
print("Age:", age)
print("Branch:", branch)
print("Grade:", grade)

# ==========================
# Q7. count() Method
# ==========================

grades = ('A', 'B', 'A', 'C', 'A', 'B', 'D', 'A', 'B')

print("Count of A:", grades.count('A'))
print("Count of B:", grades.count('B'))

grade = input("Enter a grade: ")

print(f"Count of {grade}:", grades.count(grade))

# ==========================
# Q8. index() Method
# ==========================

fruits = ('apple', 'banana', 'cherry', 'banana', 'mango', 'apple')

print("First index of banana:", fruits.index('banana'))

print("Index of banana from index 2:",
      fruits.index('banana', 2))

try:
    print("Index of kiwi:", fruits.index('kiwi'))
except ValueError:
    print("Not found")

# ==========================
# Q9. Immutability of Tuples
# ==========================

coordinates = (10, 20)

print("Original Tuple:", coordinates)

# Tuples are immutable

# coordinates[0] = 100
# Error: TypeError
# Tuples do not support item assignment.

# coordinates.append(30)
# Error: AttributeError
# Tuples do not have an append() method.

# Correct way: Convert tuple to list

temp = list(coordinates)

temp[0] = 100
temp.append(30)

coordinates = tuple(temp)

print("Modified Tuple:", coordinates)

# ==========================
# Q10. Student Record Program
# ==========================

# Input student details
name = input("Enter Name: ")
roll_no = int(input("Enter Roll Number: "))
mark1 = int(input("Enter Subject 1 Marks: "))
mark2 = int(input("Enter Subject 2 Marks: "))
mark3 = int(input("Enter Subject 3 Marks: "))

# Store data using tuple packing
student1 = name, roll_no, mark1, mark2, mark3

# Display complete record
print("\nStudent Record:", student1)

# Unpack the tuple
name, roll_no, m1, m2, m3 = student1

# Display unpacked values
print("\nStudent Details")
print("Name:", name)
print("Roll Number:", roll_no)
print("Subject 1 Marks:", m1)
print("Subject 2 Marks:", m2)
print("Subject 3 Marks:", m3)

# Count occurrence of a particular mark
mark = int(input("\nEnter mark to count: "))
print("Occurrences:", student1.count(mark))

# Create another student record
student2 = ("Devansh", 102, 78, 85, 90)

# Nested tuple containing multiple student records
students = (student1, student2)

print("\nAll Student Records:")
print(students)

# Access specific values
print("\nFirst Student Name:", students[0][0])
print("Second Student Roll Number:", students[1][1])
print("Second Student Subject 2 Marks:", students[1][3])




























