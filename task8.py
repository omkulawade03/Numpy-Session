# ==========================
# Q1. Creating Sets
# ==========================

# a) Set with 5 integers
set1 = {10, 20, 30, 40, 50}
print("Set with 5 integers:", set1)
print("Type:", type(set1))

#==========================
# b) Set with mixed data types
set2 = {100, "Python", 3.14}
print("\nMixed data type set:", set2)
print("Type:", type(set2))

#==========================
# c) Empty set (use set(), not {})
set3 = set()
print("\nEmpty set:", set3)
print("Type:", type(set3))

#==========================
# d) Set from the string "hello"
set4 = set("hello")
print("\nSet from string:", set4)
print("Type:", type(set4))

#==========================
# Sets automatically remove duplicates
# because a set stores only unique values.

example_set = {1, 2, 2, 3, 4, 4, 5}
print("\nSet after removing duplicates:", example_set)

#==========================
# Q2. Characteristics of Sets
# ==========================

# Creating a set with duplicate values
numbers = {10, 20, 30, 20, 40, 10, 50}

# Duplicates (10 and 20) are removed automatically
print("Set:", numbers)

#==========================
# Sets are unordered
# The order of elements is not guaranteed

print("First print :", numbers)
print("Second print:", numbers)
print("Third print :", numbers)

#==========================
# Trying to access an element using indexing

# print(numbers[0])

# Error:
# TypeError: 'set' object is not subscriptable
# Explanation:
# Sets do not support indexing because they are unordered.
# Therefore, elements cannot be accessed using positions like [0], [1], etc.

#==========================
# Q3. Membership Testing
#==========================
# Taking 5 colors as input from the user
color1 = input("Enter color 1: ")
color2 = input("Enter color 2: ")
color3 = input("Enter color 3: ")
color4 = input("Enter color 4: ")
color5 = input("Enter color 5: ")

# Creating a set
colors = {color1, color2, color3, color4, color5}

# Display the set
print("\nColors Set:", colors)

# Asking the user for a color to check
search_color = input("Enter a color name to check: ")

# Checking membership
if search_color in colors:
    print(search_color, "is present in the set.")

if search_color not in colors:
    print(search_color, "is not present in the set.")

#==========================
# Q4. add(), remove(), discard()
#==========================

# Creating a set
fruits = {'apple', 'banana', 'mango'}
print("Original Set:", fruits)

#==========================
# a) Add 'orange' using add()
fruits.add('orange')
print("After adding 'orange':", fruits)

#==========================
# b) Add 'banana' again
# No change because sets do not allow duplicates
fruits.add('banana')
print("After adding 'banana' again:", fruits)

#==========================
# c) Remove 'mango' using remove()
fruits.remove('mango')
print("After removing 'mango':", fruits)

#==========================
# d) Try to remove 'grape' using discard()
# No error occurs even if the element is not present
fruits.discard('grape')
print("After discarding 'grape':", fruits)

#==========================
# Q5. pop() and clear()
#==========================

# Creating a set
s = {100, 200, 300, 400, 500}
print("Original Set:", s)

#==========================
# Remove and print one element using pop()
removed_element = s.pop()
print("Popped Element:", removed_element)

# Print set after pop()
print("Set after pop():", s)

#==========================
# Clear the entire set
s.clear()

# Print final empty set
print("Set after clear():", s)

#==========================
# Q6. update() and copy()
#==========================

set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

# Make a copy of set1
copy_set = set1.copy()

# Update set1 with set2
set1.update(set2)

print("Original Copy:", copy_set)
print("Updated Set1 :", set1)


#==========================
# Q7. Union and Intersection
#==========================

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union: combines all unique elements
print("Union using union():", A.union(B))
print("Union using | :", A | B)

# Intersection: common elements in both sets
print("Intersection using intersection():", A.intersection(B))
print("Intersection using & :", A & B)

#==========================
# Q8. Combined Methods
#==========================


# Taking 6 numbers as input
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))
n5 = int(input("Enter number 5: "))
n6 = int(input("Enter number 6: "))

numbers = {n1, n2, n3, n4, n5, n6}

# Add two more numbers
numbers.add(int(input("Enter number to add: ")))
numbers.add(int(input("Enter another number to add: ")))

# Remove one number safely
remove_num = int(input("Enter number to discard: "))
numbers.discard(remove_num)

# Print final set and length
print("Final Set:", numbers)
print("Length of Set:", len(numbers))

#==========================
# Q9. Remove Duplicate Marks
#==========================

scores = [85, 92, 78, 92, 85, 88, 95, 78]

# Convert list to set
unique_scores = set(scores)

print("Unique Scores:", unique_scores)

# Convert back to sorted list
sorted_scores = sorted(unique_scores)

print("Sorted Unique Scores:", sorted_scores)

# Total unique scores
print("Total Unique Scores:", len(unique_scores))

#==========================
# Q10. Unique Item Collector
#==========================

items = set()

while True:
    print("\n===== MENU =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show All Items")
    print("4. Check Item")
    print("5. Clear All Items")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        items.add(item)
        print("Item added.")

    elif choice == "2":
        item = input("Enter item to remove: ")
        items.discard(item)
        print("Item removed if it existed.")

    elif choice == "3":
        print("Unique Items:", items)

    elif choice == "4":
        item = input("Enter item to check: ")
        if item in items:
            print("Item exists.")
        else:
            print("Item not found.")

    elif choice == "5":
        items.clear()
        print("All items cleared.")

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")

        


















