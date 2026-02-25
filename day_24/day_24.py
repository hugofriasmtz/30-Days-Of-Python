
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================================
# IMPORTING AND CHECKING VERSION
# ============================================================================

# How to import numpy
import numpy as np
# How to check the version of the numpy package
print('numpy:', np.__version__)
# Checking the available methods - uncomment to see all methods
# print(dir(np))

# ============================================================================
# CREATING INT NUMPY ARRAYS
# ============================================================================

print("\n--- Creating int numpy arrays ---")
# Creating python List
python_list = [1, 2, 3, 4, 5]

# Checking data types
print('Type:', type(python_list))  # <class 'list'>
print(python_list)  # [1, 2, 3, 4, 5]

two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Creating Numpy(Numerical Python) array from python list
numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))  # <class 'numpy.ndarray'>
print(numpy_array_from_list)  # array([1, 2, 3, 4, 5])

# ============================================================================
# CREATING FLOAT NUMPY ARRAYS
# ============================================================================

print("\n--- Creating float numpy arrays ---")
# Python list
python_list = [1, 2, 3, 4, 5]

numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2)  # array([1., 2., 3., 4., 5.])

# ============================================================================
# CREATING BOOLEAN NUMPY ARRAYS
# ============================================================================

print("\n--- Creating boolean numpy arrays ---")
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)  # array([False,  True,  True, False, False])

# ============================================================================
# CREATING MULTIDIMENSIONAL ARRAYS
# ============================================================================

print("\n--- Creating multidimensional arrays ---")
two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

# ============================================================================
# CONVERTING NUMPY ARRAY TO LIST
# ============================================================================

print("\n--- Converting numpy array to list ---")
# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# ============================================================================
# CREATING NUMPY ARRAY FROM TUPLE
# ============================================================================

print("\n--- Creating numpy array from tuple ---")
# Numpy array from tuple
# Creating tuple in Python
python_tuple = (1, 2, 3, 4, 5)
print(type(python_tuple))  # <class 'tuple'>
print('python_tuple: ', python_tuple)  # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple))  # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple)  # numpy_array_from_tuple:  [1 2 3 4 5]

# ============================================================================
# SHAPE OF NUMPY ARRAYS
# ============================================================================

print("\n--- Shape of numpy arrays ---")
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)

numpy_two_dimensional_list = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)

three_by_four_array = np.array([[0, 1, 2, 3],
                                [4, 5, 6, 7],
                                [8, 9, 10, 11]])
print(three_by_four_array)
print('shape of three_by_four_array: ', three_by_four_array.shape)

# ============================================================================
# DATA TYPE OF NUMPY ARRAYS
# ============================================================================

print("\n--- Data type of numpy arrays ---")
int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

# ============================================================================
# SIZE OF A NUMPY ARRAY
# ============================================================================

print("\n--- Size of numpy arrays ---")
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                                 [3, 4, 5],
                                 [6, 7, 8]])

print('The size:', numpy_array_from_list.size)  # 5
print('The size:', two_dimensional_list.size)  # 9

# ============================================================================
# MATHEMATICAL OPERATIONS USING NUMPY
# ============================================================================

print("\n--- Mathematical Operations ---")
# Addition
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list + 10
print("Addition (+10):", ten_plus_original)

# Subtraction
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_minus_original = numpy_array_from_list - 10
print("Subtraction (-10):", ten_minus_original)

# Multiplication
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print("Multiplication (*10):", ten_times_original)

# Division
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list / 10
print("Division (/10):", ten_times_original)

# Modulus
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
print("Modulus (%3):", ten_times_original)

# Floor Division
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print("Floor Division (//10):", ten_times_original)

# Exponential
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list ** 2
print("Exponential (**2):", ten_times_original)

# ============================================================================
# CHECKING DATA TYPES
# ============================================================================

print("\n--- Checking data types ---")
# Int, Float numbers
numpy_int_arr = np.array([1, 2, 3, 4])
numpy_float_arr = np.array([1.1, 2.0, 3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

# ============================================================================
# CONVERTING DATA TYPES
# ============================================================================

print("\n--- Converting data types ---")
# Int to Float
numpy_int_arr = np.array([1, 2, 3, 4], dtype='float')
print("Int to Float:", numpy_int_arr)

# Float to Int
numpy_int_arr = np.array([1., 2., 3., 4.], dtype='int')
print("Float to Int:", numpy_int_arr)

# Int to boolean
print("Int to boolean:", np.array([-3, -2, 0, 1, 2, 3], dtype='bool'))

# Float array for conversion demo
numpy_float_list = np.array([1.1, 2.2, 3.3])
print("Float to String:", numpy_float_list.astype('int').astype('str'))

# ============================================================================
# MULTI-DIMENSIONAL ARRAYS
# ============================================================================

print("\n--- Multi-dimensional arrays ---")
# 2 Dimension Array
two_dimension_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(type(two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

# ============================================================================
# GETTING ITEMS FROM A NUMPY ARRAY
# ============================================================================

print("\n--- Getting items from numpy array ---")
# 2 Dimension Array
two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

first_column = two_dimension_array[:, 0]
second_column = two_dimension_array[:, 1]
third_column = two_dimension_array[:, 2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)

# ============================================================================
# SLICING NUMPY ARRAYS
# ============================================================================

print("\n--- Slicing numpy arrays ---")
two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)

# Reverse the entire array
print("Reversed array:")
print(two_dimension_array[::-1, ::-1])

# ============================================================================
# REPRESENTING MISSING VALUES
# ============================================================================

print("\n--- Representing missing values ---")
two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_dimension_array)
two_dimension_array[1, 1] = 55
two_dimension_array[1, 2] = 44
print(two_dimension_array)

# Numpy Zeroes
numpy_zeroes = np.zeros((3, 3), dtype=int, order='C')
print("Zeroes array:")
print(numpy_zeroes)

# Numpy Ones
numpy_ones = np.ones((3, 3), dtype=int, order='C')
print("Ones array:")
print(numpy_ones)

twoes = numpy_ones * 2
print("Twos array:")
print(twoes)

# ============================================================================
# RESHAPE
# ============================================================================

print("\n--- Reshape ---")
first_shape = np.array([(1, 2, 3), (4, 5, 6)])
print("Original shape:", first_shape)
reshaped = first_shape.reshape(3, 2)
print("Reshaped (3,2):")
print(reshaped)

flattened = reshaped.flatten()
print("Flattened:")
print(flattened)

# ============================================================================
# HORIZONTAL AND VERTICAL STACKING
# ============================================================================

print("\n--- Stacking arrays ---")
np_list_one = np.array([1, 2, 3])
np_list_two = np.array([4, 5, 6])

print("Addition of arrays:", np_list_one + np_list_two)
print('Horizontal Stack:', np.hstack((np_list_one, np_list_two)))
print('Vertical Stack:')
print(np.vstack((np_list_one, np_list_two)))

# ============================================================================
# GENERATING RANDOM NUMBERS
# ============================================================================

print("\n--- Generating random numbers ---")
# Generate a random float number
random_float = np.random.random()
print("Random float:", random_float)

# Generate multiple random float numbers
random_floats = np.random.random(5)
print("Random floats:", random_floats)

# Generating a random integer between 0 and 10
random_int = np.random.randint(0, 11)
print("Random int:", random_int)

# Generating random integers between 2 and 11, creating a one row array
random_int = np.random.randint(2, 10, size=4)
print("Random ints (1D):", random_int)

# Generating random integers in 2D
random_int = np.random.randint(2, 10, size=(3, 3))
print("Random ints (2D):")
print(random_int)

# ============================================================================
# MATRIX IN NUMPY
# ============================================================================

print("\n--- Matrix operations ---")
four_by_four_matrix = np.matrix(np.ones((4, 4), dtype=float))
print("Matrix:")
print(four_by_four_matrix)

np.asarray(four_by_four_matrix)[2] = 2
print("Matrix after modification:")
print(four_by_four_matrix)

# ============================================================================
# NUMPY.ARANGE()
# ============================================================================

print("\n--- numpy.arange() ---")
# Creating list using range
lst = range(0, 11, 2)
print("Python range:", list(lst))

# Similar to range, numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
print("Whole numbers:", whole_numbers)

natural_numbers = np.arange(1, 20, 1)
print("Natural numbers:", natural_numbers)

odd_numbers = np.arange(1, 20, 2)
print("Odd numbers:", odd_numbers)

even_numbers = np.arange(2, 20, 2)
print("Even numbers:", even_numbers)

# ============================================================================
# CREATING SEQUENCES USING LINSPACE
# ============================================================================

print("\n--- Creating sequences with linspace ---")
# numpy.linspace()
lin_space = np.linspace(1.0, 5.0, num=10)
print("Linspace (1 to 5, 10 points):", lin_space)

# Not including the last value
lin_space = np.linspace(1.0, 5.0, num=5, endpoint=False)
print("Linspace (1 to 5, 5 points, no endpoint):", lin_space)

# ============================================================================
# LOGSPACE
# ============================================================================

print("\n--- Creating sequences with logspace ---")
log_space = np.logspace(2, 4.0, num=4)
print("Logspace:", log_space)

# ============================================================================
# ITEM SIZE OF ARRAY
# ============================================================================

print("\n--- Item size of array ---")
x = np.array([1, 2, 3], dtype=np.complex128)
print("Array:", x)
print("Item size:", x.itemsize)

# ============================================================================
# INDEXING AND SLICING
# ============================================================================

print("\n--- Indexing and slicing ---")
np_list = np.array([(1, 2, 3), (4, 5, 6)])
print(np_list)
print('First row: ', np_list[0])
print('Second row: ', np_list[1])

print('First column: ', np_list[:, 0])
print('Second column: ', np_list[:, 1])
print('Third column: ', np_list[:, 2])

# ============================================================================
# NUMPY STATISTICAL FUNCTIONS
# ============================================================================

print("\n--- Statistical functions ---")
# Using the two_dimension_array we modified earlier
two_dimension_array = np.array([[1, 2, 3], [4, 55, 44], [7, 8, 9]])
print("Array:")
print(two_dimension_array)
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ', two_dimension_array.mean())
print('std: ', two_dimension_array.std())

# Min and Max by axis
print('Column with minimum: ', np.amin(two_dimension_array, axis=0))
print('Column with maximum: ', np.amax(two_dimension_array, axis=0))
print('Row with minimum: ', np.amin(two_dimension_array, axis=1))
print('Row with maximum: ', np.amax(two_dimension_array, axis=1))

# ============================================================================
# CREATING REPEATING SEQUENCES
# ============================================================================

print("\n--- Repeating sequences ---")
a = [1, 2, 3]
print('Tile:   ', np.tile(a, 2))
print('Repeat: ', np.repeat(a, 2))

# ============================================================================
# GENERATING RANDOM NUMBERS (NORMAL DISTRIBUTION)
# ============================================================================

print("\n--- Random numbers with normal distribution ---")
# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)
print("Normal distribution sample (first 10):", normal_array[:10])

# One random number between [0,1)
one_random_num = np.random.random()
print("One random number:", one_random_num)

# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2, 3])
print("Random 2D array:")
print(r)

# Random choice
print("Random choice:", np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))

# Random numbers between [0, 1] of shape 2, 2
rand = np.random.rand(2, 2)
print("Random (0,1) 2D:")
print(rand)

# Random numbers from standard normal distribution
rand2 = np.random.randn(2, 2)
print("Random normal 2D:")
print(rand2)

# Random integers between [0, 10) of shape 5,3
rand_int = np.random.randint(0, 10, size=[5, 3])
print("Random ints (5x3):")
print(rand_int)

# ============================================================================
# STATISTICS WITH SCIPY
# ============================================================================

print("\n--- Statistics with scipy ---")
from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000)  # mean, std, samples
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis, keepdims=True))
print('std: ', np.std(np_normal_dis))

# ============================================================================
# LINEAR ALGEBRA
# ============================================================================

print("\n--- Linear algebra ---")
# Dot Product
f = np.array([1, 2, 3])
g = np.array([4, 5, 3])
print("Dot product:", np.dot(f, g))

# Matrix multiplication
h = [[1, 2], [3, 4]]
i = [[5, 6], [7, 8]]
print("Matrix multiplication:")
print(np.matmul(h, i))

# Determinant
print("Determinant:", np.linalg.det(i))

# ============================================================================
# CHECKERBOARD PATTERN
# ============================================================================

print("\n--- Checkerboard pattern ---")
Z = np.zeros((8, 8))
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print(Z)

# ============================================================================
# LINEAR RELATIONSHIP
# ============================================================================

print("\n--- Linear relationship ---")
temp = np.array([1, 2, 3, 4, 5])
pressure = temp * 2 + 5
print("Temperature:", temp)
print("Pressure:", pressure)

# ============================================================================
# LIST COMPREHENSION VS NUMPY
# ============================================================================

print("\n--- List comprehension vs NumPy ---")
new_list = [x + 2 for x in range(0, 11)]
print("List comprehension:", new_list)

np_arr = np.array(range(0, 11))
np_result = np_arr + 2
print("NumPy:", np_result)

# ============================================================================
# NORMAL DISTRIBUTION VISUALIZATION
# ============================================================================

print("\n--- Creating histogram (uncomment to see plot) ---")
# Uncomment these lines to display the histogram
# mu = 28
# sigma = 15
# samples = 100000
# x = np.random.normal(mu, sigma, samples)
# ax = sns.distplot(x)
# ax.set(xlabel="x", ylabel='y')
# plt.show()

print("All examples completed successfully!")
