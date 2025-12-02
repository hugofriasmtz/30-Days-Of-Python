# Syntax Error
# print 'Hello Python'
print('Hello Python')

# NameError
age = 8
print(age)

# IndexError
numbers = [1, 2, 3, 4, 5]
# numbers[5]
numbers[4]

# ModuleNotFoundError
# import maths
import math

# AttributeError
# math.PI
print(math.pi)

# KeyError
users = {'name':'Erwin', 'age':31, 'country':'Mexico'}
name = users['name']
print(name)
# country = users['county']
country = users['country']
print(country)

# TypeError
#4 + '10'
sum = 4 + int('10')
print(sum)

# ImportError
# from math import power
from math import pow
print(pow(2,3))

# ValueError
# int('12a')

# ZeroDivisionError
# 1/0 