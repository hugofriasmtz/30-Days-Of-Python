"""
Day 24 Exercises: NumPy
Exercise: Repeat all the examples from the guide
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

print("=" * 80)
print("DAY 24: NUMPY EXERCISES - REPEATING ALL EXAMPLES")
print("=" * 80)

# ============================================================================
# 1. IMPORT NUMPY AND CHECK VERSION
# ============================================================================

print("\n1. IMPORT AND VERSION")
print("-" * 80)
print('NumPy Version:', np.__version__)

# ============================================================================
# 2. CREATE ARRAYS FROM LISTS
# ============================================================================

print("\n2. CREATE ARRAYS FROM LISTS")
print("-" * 80)
python_list = [1, 2, 3, 4, 5]
numpy_array = np.array(python_list)
print(f"Python list: {python_list}")
print(f"NumPy array: {numpy_array}")
print(f"Array dtype: {numpy_array.dtype}")

# Create float array
float_array = np.array(python_list, dtype=float)
print(f"Float array: {float_array}")

# Create boolean array
bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(f"Boolean array: {bool_array}")

# ============================================================================
# 3. MULTIDIMENSIONAL ARRAYS
# ============================================================================

print("\n3. MULTIDIMENSIONAL ARRAYS")
print("-" * 80)
two_d_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
two_d_array = np.array(two_d_list)
print("2D Array:")
print(two_d_array)
print(f"Shape: {two_d_array.shape}")
print(f"Size: {two_d_array.size}")

# ============================================================================
# 4. CONVERT ARRAY TO LIST
# ============================================================================

print("\n4. CONVERT ARRAY TO LIST")
print("-" * 80)
back_to_list = numpy_array.tolist()
print(f"Array to list: {back_to_list}")
print(f"Type: {type(back_to_list)}")

# ============================================================================
# 5. CREATE FROM TUPLE
# ============================================================================

print("\n5. CREATE FROM TUPLE")
print("-" * 80)
python_tuple = (1, 2, 3, 4, 5)
tuple_array = np.array(python_tuple)
print(f"Tuple: {python_tuple}")
print(f"Array from tuple: {tuple_array}")

# ============================================================================
# 6. ARRAY SHAPE
# ============================================================================

print("\n6. ARRAY SHAPE")
print("-" * 80)
arr_1d = np.array([1, 2, 3, 4, 5])
print(f"1D array shape: {arr_1d.shape}")

arr_2d = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(f"2D array shape: {arr_2d.shape}")

arr_3d = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
print(f"3x4 array shape: {arr_3d.shape}")

# ============================================================================
# 7. DATA TYPES
# ============================================================================

print("\n7. DATA TYPES AND CONVERSION")
print("-" * 80)
int_arr = np.array([-3, -2, -1, 0, 1, 2, 3])
print(f"Int array: {int_arr}, dtype: {int_arr.dtype}")

float_arr = int_arr.astype(float)
print(f"Float array: {float_arr}, dtype: {float_arr.dtype}")

back_to_int = float_arr.astype(int)
print(f"Back to int: {back_to_int}, dtype: {back_to_int.dtype}")

bool_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')
print(f"Boolean: {bool_arr}")

# ============================================================================
# 8. MATHEMATICAL OPERATIONS
# ============================================================================

print("\n8. MATHEMATICAL OPERATIONS")
print("-" * 80)
arr = np.array([1, 2, 3, 4, 5])
print(f"Original: {arr}")
print(f"Add 10: {arr + 10}")
print(f"Subtract 10: {arr - 10}")
print(f"Multiply by 10: {arr * 10}")
print(f"Divide by 10: {arr / 10}")
print(f"Modulus 3: {arr % 3}")
print(f"Floor division by 2: {arr // 2}")
print(f"Power 2: {arr ** 2}")

# ============================================================================
# 9. ARRAY INDEXING AND SLICING
# ============================================================================

print("\n9. INDEXING AND SLICING")
print("-" * 80)
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:")
print(arr_2d)
print(f"First row: {arr_2d[0]}")
print(f"Second row: {arr_2d[1]}")
print(f"First column: {arr_2d[:, 0]}")
print(f"Second column: {arr_2d[:, 1]}")

# Slicing
print("First 2 rows, first 2 cols:")
print(arr_2d[0:2, 0:2])

# Reverse
print("Reversed array:")
print(arr_2d[::-1, ::-1])

# ============================================================================
# 10. SPECIAL ARRAYS (ZEROS, ONES)
# ============================================================================

print("\n10. SPECIAL ARRAYS")
print("-" * 80)
zeros = np.zeros((3, 3), dtype=int)
print("Zeros:")
print(zeros)

ones = np.ones((3, 3), dtype=int)
print("Ones:")
print(ones)

twos = ones * 2
print("Twos:")
print(twos)

# ============================================================================
# 11. RESHAPE AND FLATTEN
# ============================================================================

print("\n11. RESHAPE AND FLATTEN")
print("-" * 80)
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original shape {arr.shape}:")
print(arr)

reshaped = arr.reshape(3, 2)
print(f"Reshaped to (3, 2):")
print(reshaped)

flattened = reshaped.flatten()
print(f"Flattened: {flattened}")

# ============================================================================
# 12. STACKING ARRAYS
# ============================================================================

print("\n12. STACKING ARRAYS")
print("-" * 80)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
print(f"Addition: {arr1 + arr2}")
print(f"Horizontal stack: {np.hstack((arr1, arr2))}")
print("Vertical stack:")
print(np.vstack((arr1, arr2)))

# ============================================================================
# 13. ARANGE
# ============================================================================

print("\n13. ARANGE")
print("-" * 80)
whole_nums = np.arange(0, 20, 1)
print(f"Whole numbers (0-19): {whole_nums}")

odd_nums = np.arange(1, 20, 2)
print(f"Odd numbers: {odd_nums}")

even_nums = np.arange(2, 20, 2)
print(f"Even numbers: {even_nums}")

# ============================================================================
# 14. LINSPACE
# ============================================================================

print("\n14. LINSPACE")
print("-" * 80)
lin = np.linspace(1.0, 5.0, num=10)
print(f"10 values from 1 to 5: {lin}")

lin_no_end = np.linspace(1.0, 5.0, num=5, endpoint=False)
print(f"5 values from 1 to 5 (no endpoint): {lin_no_end}")

# ============================================================================
# 15. LOGSPACE
# ============================================================================

print("\n15. LOGSPACE")
print("-" * 80)
log_vals = np.logspace(2, 4.0, num=4)
print(f"Logspace (10^2 to 10^4, 4 points): {log_vals}")

# ============================================================================
# 16. RANDOM NUMBERS
# ============================================================================

print("\n16. RANDOM NUMBERS")
print("-" * 80)
# Float between 0 and 1
rand_float = np.random.random()
print(f"Single random float: {rand_float}")

rand_floats = np.random.random(5)
print(f"5 random floats: {rand_floats}")

# Random integers
rand_int = np.random.randint(0, 11)
print(f"Random int (0-10): {rand_int}")

rand_ints_1d = np.random.randint(2, 10, size=4)
print(f"4 random ints (2-10): {rand_ints_1d}")

rand_ints_2d = np.random.randint(0, 10, size=(3, 3))
print("3x3 random ints (0-10):")
print(rand_ints_2d)

# Choice from list
choices = np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10)
print(f"Random choice from vowels: {choices}")

# ============================================================================
# 17. NORMAL DISTRIBUTION
# ============================================================================

print("\n17. NORMAL DISTRIBUTION")
print("-" * 80)
normal_dist = np.random.normal(5, 0.5, 1000)
print(f"Normal distribution - mean: {normal_dist.mean():.2f}, std: {normal_dist.std():.2f}")
print(f"First 10 values: {normal_dist[:10]}")

# ============================================================================
# 18. STATISTICAL FUNCTIONS
# ============================================================================

print("\n18. STATISTICAL FUNCTIONS")
print("-" * 80)
arr = np.array([[1, 2, 3], [4, 55, 44], [7, 8, 9]])
print("Array:")
print(arr)
print(f"Min: {arr.min()}")
print(f"Max: {arr.max()}")
print(f"Mean: {arr.mean():.2f}")
print(f"Median: {np.median(arr):.2f}")
print(f"Std Dev: {arr.std():.2f}")
print(f"Min by column: {np.amin(arr, axis=0)}")
print(f"Max by column: {np.amax(arr, axis=0)}")
print(f"Min by row: {np.amin(arr, axis=1)}")
print(f"Max by row: {np.amax(arr, axis=1)}")

# ============================================================================
# 19. REPEATING SEQUENCES
# ============================================================================

print("\n19. REPEATING SEQUENCES")
print("-" * 80)
arr = [1, 2, 3]
print(f"Original: {arr}")
print(f"Tile (repeat array): {np.tile(arr, 2)}")
print(f"Repeat (repeat elements): {np.repeat(arr, 2)}")

# ============================================================================
# 20. LINEAR ALGEBRA
# ============================================================================

print("\n20. LINEAR ALGEBRA")
print("-" * 80)
# Dot product
f = np.array([1, 2, 3])
g = np.array([4, 5, 3])
print(f"Vector f: {f}")
print(f"Vector g: {g}")
print(f"Dot product: {np.dot(f, g)}")

# Matrix multiplication
h = [[1, 2], [3, 4]]
i = [[5, 6], [7, 8]]
print(f"Matrix h: {h}")
print(f"Matrix i: {i}")
print("Matrix product:")
print(np.matmul(h, i))

# Determinant
det = np.linalg.det(i)
print(f"Determinant of i: {det:.1f}")

# ============================================================================
# 21. MATRIX OPERATIONS
# ============================================================================

print("\n21. MATRIX OPERATIONS")
print("-" * 80)
matrix = np.matrix(np.ones((4, 4), dtype=float))
print("Original 4x4 matrix:")
print(matrix)

np.asarray(matrix)[2] = 2
print("After modifying row 2:")
print(matrix)

# ============================================================================
# 22. CHECKERBOARD PATTERN
# ============================================================================

print("\n22. CHECKERBOARD PATTERN")
print("-" * 80)
Z = np.zeros((8, 8))
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print("Checkerboard pattern:")
print(Z)

# ============================================================================
# 23. LINEAR RELATIONSHIP
# ============================================================================

print("\n23. LINEAR RELATIONSHIP")
print("-" * 80)
temp = np.array([1, 2, 3, 4, 5])
pressure = temp * 2 + 5
print(f"Temperature: {temp}")
print(f"Pressure: {pressure}")
print("(Pressure = Temperature * 2 + 5)")

# ============================================================================
# 24. SCIPY STATISTICS
# ============================================================================

print("\n24. SCIPY STATISTICS")
print("-" * 80)
np_normal_dis = np.random.normal(5, 0.5, 1000)
print(f"Min: {np.min(np_normal_dis):.2f}")
print(f"Max: {np.max(np_normal_dis):.2f}")
print(f"Mean: {np.mean(np_normal_dis):.2f}")
print(f"Median: {np.median(np_normal_dis):.2f}")
print(f"Std Dev: {np.std(np_normal_dis):.2f}")
print(f"Mode: {stats.mode(np_normal_dis, keepdims=True).mode[0]:.2f}")

# ============================================================================
# 25. ITEM SIZE
# ============================================================================

print("\n25. ITEM SIZE")
print("-" * 80)
x = np.array([1, 2, 3], dtype=np.complex128)
print(f"Complex array: {x}")
print(f"Item size in bytes: {x.itemsize}")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 80)
print("ALL EXAMPLES COMPLETED SUCCESSFULLY!")
print("=" * 80)


