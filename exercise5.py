# Week 5
# NumPy

# NumPy is imported and ready to use.
# import numpy
import numpy as np

arr = numpy.array([1, 2, 3, 4, 5])
print(arr)

# NumPy package can be referred to as np instead of numpy.
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# The version string is stored under __version__ attribute.
import numpy as np
print(np.__version__)

# NumPy Creating Arrays
# NumPy ndarray object by using the array() function.
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# tuple to create a NumPy array:
import numpy as np
arr = np.array((1, 2, 3, 4, 5))
print(arr)

# Insert the correct method for creating a NumPy array.
arr = np.array([1, 2, 3, 4, 5])

# Insert the correct argument for creating a NumPy array with 2 dimensions.
arr = np.array([1, 2, 3, 4], ndmin=2)

# Insert the correct syntax for checking the number of dimension of a NumPy array.
arr = np.array([1, 2, 3, 4])
print(arr.ndim)

# Create a 0-D array with value 42
import numpy as np
arr = np.array(42)
print(arr)

# Create a 1-D array containing the values 1,2,3,4,5:
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

# Check how many dimensions the arrays have:
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# Create an array with 5 dimensions and verify that it has 5 dimensions:
import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

# NumPy Array Indexing
# correct syntax for printing the first item in the array.
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])

# correct syntax for printing the number 50 from the array.
arr = np.array([10, 20, 30, 40, 50])
print(arr[4])

# Insert the correct syntax for printing the number 50 from the array.
arr = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print(arr[1, 0])

# Use negative index to print the last item in the array.
arr = np.array([10, 20, 30, 40, 50])
print(arr[-1])

# Numpy Slicing Arrays
# Everything from (including) the second item to (not including) the fifth item.
arr = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr[1:4])

# Everything from (including) the third item to (not including) the fifth item.
arr = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr[2:4])

# use the step syntax.
arr = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr[1:4:2])

# Every other item from the entire array.
arr = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr[::2])

# NumPy Data Type
# NumPy uses a character to represent each of the following data types, which one?
# NumPy Data Type
# NumPy uses a character to represent each of the following data types, which one?

# Mapping of NumPy data types to characters
{
    'i': 'integer',
    'b': 'boolean',
    'u': 'unsigned integer',
    'f': 'float',
    'c': 'complex float',
    'm': 'timedelta',
    'M': 'datetime',
    'O': 'object',
    'S': 'string'
}


# Insert the correct NumPy syntax to print the data type of an array.
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# correct argument to specify that the array should be of type STRING.
arr = np.array([1, 2, 3, 4], dtype='S')

#  correct method to change the data type to integer.
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')

# Numpy Copy
# correct method to make a copy of the array.
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()

# correct method to make a view of the array.
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()

# Numpy Array Shape
# correct NumPy syntax to check the shape of an array.
arr = np.array([1, 2, 3, 4, 5])
print(arr.shape)

# correct NumPy method to change the shape of an array from 1-D to 2-D.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)

# correct NumPy method to change the shape of an array from 2-D to 1-D.
arr = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
newarr = arr.reshape(-1)

# Numpy Array Join
# correct NumPy method to join two arrays into a single array.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))

# Numpy Array Search
# correct NumPy method to find all items with the value 4.
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)

# Numpy Array sort
# correct NumPy method to return a sorted array.
arr = np.array([3, 2, 0, 1])
x = np.sort(arr)

# Method 1: Creating a matrix with a List of list
matrix = [[1, 2, 3, 4], 
	[5, 6, 7, 8],
	[9, 10, 11, 12]]

print("Matrix =", matrix)

# Method 2: Take Matrix input from user in Python
Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries row wise:")

# For user input
# A for loop for row entries
for row in range(Row): 
	a = []
	# A for loop for column entries
	for column in range(Column): 
		a.append(int(input()))
	matrix.append(a)

# For printing the matrix
for row in range(Row):
	for column in range(Column):
		print(matrix[row][column], end=" ")
	print()


# Method 3: Create a matrix using list comprehension
matrix = [[column for column in range(4)] for row in range(4)]

print(matrix)


# Assigning Value in a matrix
# Here we are replacing and assigning value to an individual cell (1 row and 1 column = 11) in the Matrix.
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

row = column = 1

X[row][column] = 11

print(X)

# Method 2: Assign a value to an individual cell using negative indexing in Matrix
# Here we are replacing and assigning value to an individual cell (-2 row and -1 column = 21) in the Matrix.
row = -2
column = -1

X[row][column] = 21

print(X)

# Method 1: Accessing Matrix values
# Accessing elements of a Matrix by passing its row and column.
print("Matrix at 1 row and 3 column=", X[0][2]) 
print("Matrix at 3 row and 3 column=", X[2][2])

# Method 2: Accessing Matrix values using negative indexing
import numpy as np

X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(X[-1][-2])

# Mathematical Operations with Matrix in Python
# Adding values to a matrix with a for loop in python
# Program to add two matrices using nested loop
X = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# iterate through rows
for row in range(len(X)):

	# iterate through columns
	for column in range(len(X[0])):
		result[row][column] = X[row][column]+ Y[row][column]

for r in result:
	print(r)

# Adding and subtracting values to a matrix with list comprehension
Add_result = [[X[row][column] + Y[row][column]
			for column in range(len(X[0]))] 
			for row in range(len(X))]
Sub_result = [[X[row][column] - Y[row][column]
			for column in range(len(X[0]))] 
			for row in range(len(X))]

print("Matrix Addition")
for r in Add_result:
	print(r)

print("\nMatrix Subtraction")
for r in Sub_result:
	print(r)

# Python program to multiply and divide two matrices
rmatrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(len(X)):
	for column in range(len(X[0])):
		rmatrix[row][column] = X[row][column] * Y[row][column]
		
print("Matrix Multiplication",)
for r in rmatrix:
	print(r)
		
for i in range(len(X)):
	for j in range(len(X[0])):
		rmatrix[row][column] = X[row][column] // Y[row][column]

print("\nMatrix Division",) 
for r in rmatrix:
	print(r)

# Transpose in matrix
# Transpose a Matrix using loop
X = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# iterate through rows
for row in range(len(X)):
	# iterate through columns
	for column in range(len(X[0])):
		result[column][row] = X[row][column]

for r in result:
	print(r)
	
# # Python Program to Transpose a Matrix using the list comprehension

# rez = [[X[column][row] for column in range(len(X))] 
# for row in range(len(X[0]))]

# for row in rez:
#	 print(row)

# Matrix using Numpy
# Numpy array using numpy.random and a random module.
import numpy as np

# 1st argument --> numbers ranging from 0 to 9, 
# 2nd argument, row = 3, col = 3
array = np.random.randint(10, size=(3, 3))
print(array)

# Matrix mathematical operations in Python Using Numpy
# initializing matrices
x = numpy.array([[1, 2], [4, 5]])
y = numpy.array([[7, 8], [9, 10]])

# using add() to add matrices
print ("The element wise addition of matrix is : ")
print (numpy.add(x,y))

# using subtract() to subtract matrices
print ("The element wise subtraction of matrix is : ")
print (numpy.subtract(x,y))

print ("The element wise multiplication of matrix is : ")
print (numpy.multiply(x,y))

# using divide() to divide matrices
print ("The element wise division of matrix is : ")
print (numpy.divide(x,y))

# Dot and cross product with Matrix
X = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

Y = [[9, 8, 7], [6, 5, 4],[3, 2, 1]]

dotproduct = np.dot(X, Y)
print("Dot product of two array is:", dotproduct)

dotproduct = np.cross(X, Y)
print("Cross product of two array is:", dotproduct)

# Create an empty matrix with NumPy in Python
# Initializing an empty array, using the np.zeros().
a = np.zeros([2, 2], dtype=int)
print("\nMatrix of 2x2: \n", a)

c = np.zeros([3, 3])
print("\nMatrix of 3x3: \n", c)

# Slicing in Matrix using Numpy
X = np.array([[6, 8, 10], 
	[ 9, -12, 15],
	[ 12, 16, 20],
	[ 15, -20, 25]])

# Example of slicing 
# Syntax: Lst[ Initial: End: IndexJump ]
print(X[:])

print("\nSlicing Third Row-Second Column: ", X[2:3,1])
print("\nSlicing Third Row-Third Column: ", X[2:3,2])

# Delete rows and columns using Numpy
# create an array with integers
# with 3 rows and 4 columns
a = np.array([[6, 8, 10], 
	[ 9, -12, 15],
	[ 12, 16, 20],
	[ 15, -20, 25]])

# delete 0 th row
data = np.delete(a, 0, 0)
print("data after 0 th row deleted: ", data)

# delete 1 st row
data = np.delete(a, 1, 0)
print("\ndata after 1 st row deleted: ", data)

# delete 2 nd row
data = np.delete(a, 2, 0)
print("\ndata after 2 nd row deleted: ", data)

# Add row/columns in the Numpy array
ini_array = np.array([[6, 8, 10],
					[9, -12, 15],
					[15, -20, 25]])

# Array to be added as column
column_to_be_added = np.array([1, 2, 3])

# Adding column to numpy array
result = np.hstack((ini_array, np.atleast_2d(column_to_be_added).T))

# printing result
print("\nresultant array\n", str(result))

# Delete rows and columns using Numpy
# create an array with integers
# with 3 rows and 4 columns
a = np.array([[6, 8, 10], 
	[ 9, -12, 15],
	[ 12, 16, 20],
	[ 15, -20, 25]])

# delete 0 th row
data = np.delete(a, 0, 0)
print("data after 0 th row deleted: ", data)

# delete 1 st row
data = np.delete(a, 1, 0)
print("\ndata after 1 st row deleted: ", data)

# delete 2 nd row
data = np.delete(a, 2, 0)
print("\ndata after 2 nd row deleted: ", data)

# Add row/columns in the Numpy array
ini_array = np.array([[6, 8, 10],
					[9, -12, 15],
					[15, -20, 25]])

# Array to be added as column
column_to_be_added = np.array([1, 2, 3])

# Adding column to numpy array
result = np.hstack((ini_array, np.atleast_2d(column_to_be_added).T))

# printing result
print("\nresultant array\n", str(result))


