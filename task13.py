import numpy as np

# ==========================
# Q1. Basic Array Creation
# ==========================

# Create 1D array
arr1 = np.array([10, 20, 30, 40, 50])

# Create 2D array
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("1D Array:")
print(arr1)
print("Shape:", arr1.shape)
print("Data Type:", arr1.dtype)

print("2D Array:")
print(arr2)
print("Shape:", arr2.shape)
print("Data Type:", arr2.dtype)


# ==========================
# Q2. Zeros and Ones
# ==========================

zeros_1d = np.zeros(8)
ones_2d = np.ones((4, 4))
zeros_3x3 = np.zeros((3, 3))

print("1D Zeros Array:")
print(zeros_1d)

print("4x4 Ones Array:")
print(ones_2d)

print("3x3 Zeros Matrix:")
print(zeros_3x3)


# ==========================
# Q3. np.arange()
# ==========================

a = np.arange(0, 21, 1)
b = np.arange(10, 51, 2)
c = np.arange(5, 101, 5)

print("(a):", a)
print("(b):", b)
print("(c):", c)


# ==========================
# Q4. np.linspace()
# ==========================

line1 = np.linspace(0, 5, 10)
line2 = np.linspace(-10, 10, 15)

print("(a):", line1)
print("Length:", len(line1))

print("(b):", line2)
print("Length:", len(line2))


# ==========================
# Q5. Random Arrays
# ==========================

rand1 = np.random.rand(10)
rand2 = np.random.randn(3, 3)
rand3 = np.random.randint(10, 51, (4, 5))

print("(a) Random Numbers:")
print(rand1)

print("(b) Random Normal Matrix:")
print(rand2)

print("(c) Random Integer Matrix:")
print(rand3)


# ==========================
# Q6. Vectors and Operations
# ==========================

v1 = np.array([2, 4, 6, 8])
v2 = np.array([1, 3, 5, 7])

print("Addition:")
print(v1 + v2)

print("Subtraction:")
print(v1 - v2)

print("Element-wise Multiplication:")
print(v1 * v2)

print("Dot Product:")
print(np.dot(v1, v2))


# ==========================
# Q7. Matrices and Operations
# ==========================

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print("Matrix Addition:")
print(A + B)

print("Matrix Multiplication:")
print(A @ B)

print("Element-wise Multiplication:")
print(A * B)



# ==========================
# Q8. Properties of Arrays
# ==========================

matrix = np.random.randint(1, 101, (4, 4))

print("Matrix:")
print(matrix)

print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Size:", matrix.size)
print("Data Type:", matrix.dtype)
print("Minimum:", matrix.min())
print("Maximum:", matrix.max())


# ==========================
# Q9. Random + Reshape + Statistics
# ==========================

arr = np.random.randint(1, 51, 20)

matrix_4x5 = arr.reshape(4, 5)

print("4x5 Matrix:")
print(matrix_4x5)

print("Sum:", np.sum(matrix_4x5))
print("Mean:", np.mean(matrix_4x5))
print("Standard Deviation:", np.std(matrix_4x5))

print("Maximum Value in Each Row:")
print(np.max(matrix_4x5, axis=1))


# ==========================
# Q10. Mini Project - Statistics Calculator
# ==========================

try:
    n = int(input("\nEnter how many random numbers to generate: "))

    numbers = np.random.randint(10, 101, n)

    print("\nGenerated Array:")
    print(numbers)

    print("\nMean:", np.mean(numbers))
    print("Median:", np.median(numbers))
    print("Standard Deviation:", np.std(numbers))
    print("Minimum:", np.min(numbers))
    print("Maximum:", np.max(numbers))

    # Reshape if possible
    if n % 2 == 0:
        reshaped = numbers.reshape(2, n // 2)

        print("\nReshaped Array:")
        print(reshaped)

        print("\nRow-wise Sum:")
        print(np.sum(reshaped, axis=1))
    else:
        print("\nReshaping not possible into 2 rows.")

except ValueError:
    print("Please enter a valid number.")




