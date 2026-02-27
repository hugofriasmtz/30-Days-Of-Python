import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np

# Creating Pandas Series with Default Index
nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)

# Creating Pandas Series with custom index
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

# Creating Pandas Series from a Dictionary
dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}

s = pd.Series(dct)
print(s)

# Creating a Constant Pandas Series
s = pd.Series(10, index = [1, 2, 3])
print(s)

# Creating a Pandas Series Using Linspace
s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)

# =============================
# DataFrames
# =============================

# Creating DataFrames from List of Lists
data = [
    ['Asabeneh', 'Finland', 'Helsink'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

# Creating DataFrame Using Dictionary
data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

# Creating DataFrames from a List of Dictionaries
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)

# =============================
# Reading CSV File Using Pandas
# =============================

df = pd.read_csv('./data/weight-height.csv')
print(df)

# Data Exploration
print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method
print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method
print(df.shape) # as you can see 10000 rows and three columns

print(df.columns)

heights = df['Height'] # this is now a series
print(heights)

weights = df['Weight'] # this is now a series
print(weights)

print(len(heights) == len(weights))

print(heights.describe()) # give statistical information about height data
print(weights.describe()) # give statistical information about weights data

# =============================
# Modifying a DataFrame
# =============================

data = [
    {"Name": "Erwin", "Country":"Finland","City":"Helsinki"},
    {"Name": "Oscar", "Country":"UK","City":"London"},
    {"Name": "Cesar", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)

# Adding new column
weights = [74, 78, 69]
df['Weight'] = weights
df

heights = [173, 175, 169]
df['Height'] = heights
print(df)

# Modifying column values
df['Height'] = df['Height'] * 0.01
df

# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi

bmi = calculate_bmi()

df['BMI'] = bmi
df

# Formatting DataFrame columns
df['BMI'] = round(df['BMI'], 1)
print(df)

birth_year = ['1994', '2018', '2023']
current_year = pd.Series(2026, index=[0, 1, 2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
print(df)

# =============================
# Checking data types of Column values
# =============================

print(df.Weight.dtype)

df['Birth Year'].dtype # it gives string object , we should change this to number
df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype) # let's check the data type now

df['Current Year'] = df['Current Year'].astype('int')
df['Current Year'].dtype

ages = df['Current Year'] - df['Birth Year']
ages

df['Ages'] = ages
print(df)

mean = (35 + 30)/ 2
print('Mean: ',mean)	#it is good to add some description to the output, so we know what is what

# =============================
# Boolean Indexing
# =============================

print(df[df['Ages'] > 10])
print(df[df['Ages'] < 10])