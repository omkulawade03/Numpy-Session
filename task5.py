# ==========================
# Q1
# String Indexing
# ==========================
text = input("Enter a string: ")

print("First character:", text[0])
print("3rd character:", text[2])

print("Last character:", text[-1])
print("2nd character from the end:", text[-2])


# ==========================
# Q2
# String Slicing
# ==========================
text = input("Enter a string: ")

print("First 5 characters:", text[:5])
print("Last 4 characters:", text[-4:])
print("Reverse string:", text[::-1])
print("Every 2nd character:", text[::2])


# ==========================
# Q3
# Membership Operators
# ==========================
main_string = input("Enter the main string: ")
substring = input("Enter the substring: ")

if substring in main_string:
    print("Substring found!")
else:
    print("Substring not found!")

if substring not in main_string:
    print("Substring is not present in the main string.")


# ==========================
# Q4
# len() Function
# ==========================
text = input("Enter a string: ")

length = len(text)
print("Length of the string:", length)

print("Last character:", text[length - 1])

if length % 2 != 0:
    print("Middle character:", text[length // 2])
else:
    print("String length is even, no single middle character.")


# ==========================
# Q5
# range() Function
# ==========================
print("Numbers from 0 to 10:")
print(list(range(11)))

print("Numbers from 5 to 15:")
print(list(range(5, 16)))

print("Odd numbers from 1 to 21:")
print(list(range(1, 22, 2)))


# ==========================
# Q6
# Negative Step in range()
# ==========================
print("Numbers from 20 down to 10:")
print(list(range(20, 9, -1)))

print("Numbers from 15 down to 1 in steps of 2:")
print(list(range(15, 0, -2)))


# ==========================
# Q7
# String Traversal
# ==========================
text = input("Enter a string: ")

print("Characters with index:")
for i in range(len(text)):
    print(i, ":", text[i])

print("String in reverse order:")
for i in range(len(text) - 1, -1, -1):
    print(text[i], end="")


# ==========================
# Q8
# Number in Range Check
# ==========================
num = int(input("\nEnter a number: "))

if num in range(1, 51):
    print("The number is present in range(1, 51).")
else:
    print("The number is NOT present in range(1, 51).")

if num in range(10, 100, 5):
    print("The number is present in range(10, 100, 5).")
else:
    print("The number is NOT present in range(10, 100, 5).")


# ==========================
# Q9
# Range and String Slicing Practice
# ==========================
print("First 10 even numbers:")
print(list(range(2, 21, 2)))

print("Numbers from 1 to 30 in steps of 3:")
print(list(range(1, 31, 3)))

text = "PythonProgramming"

print("Python:", text[:6])
print("Programming:", text[6:])
print("Reverse:", text[::-1])


# ==========================
# Q10
# Mini Project
# ==========================
user_string = input("Enter a string: ")

length = len(user_string)
print("Length:", length)

mid = length // 2
print("First half:", user_string[:mid])
print("Second half:", user_string[mid:])

if "python" in user_string.lower():
    print("'python' is present.")
else:
    print("'python' is not present.")

print("Positive indices:", list(range(length)))
print("Negative indices:", list(range(-length, 0)))

print("Reverse string:", user_string[::-1])













