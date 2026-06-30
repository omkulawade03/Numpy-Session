# ==========================
# Q1
# Creating Lists
# ==========================
integer_list = [10, 20, 30, 40, 50]

empty_list1 = []
empty_list2 = list()

mixed_list = [25, "Python", 3.14, True]

zero_list = [0] * 7

print("Integer List:", integer_list)
print("Empty List []:", empty_list1)
print("Empty List list():", empty_list2)
print("Mixed List:", mixed_list)
print("Zero List:", zero_list)


# ==========================
# Q2
# List Indexing
# ==========================
fruits = ["apple", "banana", "mango", "orange", "grape"]

print("First item:", fruits[0])
print("Third item:", fruits[2])

print("Last item:", fruits[-1])
print("Second last item:", fruits[-2])

index = int(input("Enter an index number: "))

if index >= 0 and index < len(fruits):
    print("Item at index", index, "is:", fruits[index])
else:
    print("Invalid index!")


# ==========================
# Q3
# List Slicing
# ==========================
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("First 4 elements:", numbers[:4])
print("Last 3 elements:", numbers[-3:])
print("Elements from index 2 to 7:", numbers[2:8])
print("Every second element:", numbers[::2])
print("Reversed list:", numbers[::-1])


# ==========================
# Q4
# Updating List Elements
# ==========================
colors = ["red", "blue", "green", "yellow"]

colors[1] = "purple"
print("After changing blue to purple:", colors)

colors[-1] = "black"
print("After changing last item to black:", colors)


# ==========================
# Q5
# Adding Elements to List
# ==========================
cities = []

city1 = input("Enter first city: ")
city2 = input("Enter second city: ")

cities.append(city1)
cities.append(city2)
cities.append("Mumbai")
cities.append("Delhi")
cities.append("Chennai")

cities.insert(2, "Pune")

print("Final List of Cities:", cities)


# ==========================
# Q6
# Removing Elements from List
# ==========================
items = [10, 20, 30, 20, 40, 50]

items.remove(20)
print("After remove(20):", items)

removed_item = items.pop(3)
print("Removed item at index 3:", removed_item)
print("List after pop(3):", items)

last_item = items.pop()
print("Removed last item:", last_item)
print("List after removing last item:", items)

items.clear()
print("List after clear():", items)


# ==========================
# Q7
# Searching in List
# ==========================
scores = [85, 92, 78, 92, 65, 92, 88]

print("Index of first 92:", scores.index(92))
print("Count of 92:", scores.count(92))

num = int(input("Enter a number: "))

if num in scores:
    print("Number found!")
    print("Index:", scores.index(num))
    print("Count:", scores.count(num))
else:
    print("Number not found in the list.")


# ==========================
# Q8
# Sorting and Reversing Lists
# ==========================
marks = [45, 78, 65, 90, 34, 82, 71]

marks.sort()
print("Ascending order:", marks)

marks.sort(reverse=True)
print("Descending order:", marks)

marks2 = [45, 78, 65, 90, 34, 82, 71]

marks2.reverse()
print("Reversed original list:", marks2)


# ==========================
# Q9
# Combining Lists
# ==========================
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list_extend = list1.copy()
list_extend.extend(list2)
print("Using extend():", list_extend)

list_append = list1.copy()
list_append.append(list2)
print("Using append():", list_append)


# ==========================
# Q10
# Student Marks Manager
# ==========================
marks = []

for i in range(5):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

print("Marks List:", marks)

extra_mark = int(input("Enter marks for one more subject: "))
marks.append(extra_mark)

print("Updated Marks List:", marks)

print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))

marks.sort(reverse=True)
print("Marks in Descending Order:", marks)

average = sum(marks) / len(marks)
print("Average Marks:", average)

print("Total Subjects:", len(marks))