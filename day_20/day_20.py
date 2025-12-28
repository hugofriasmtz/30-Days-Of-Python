# =============================
# Installing PIP
# =============================

# pip install pip
# pip --version

# =============================
# Installing packages using pip
# =============================

# pip install numpy

import numpy
import pandas
import webbrowser # web browser module to open websites

lst = [1, 2, 3,4, 5]
np_arr = numpy.array(lst)
np_arr
print(np_arr)
print(len(np_arr))

print(np_arr * 2)
print(np_arr + 2)


# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/hugofrias/',
    'https://github.com/hugofriasmtz',
    
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)

# =============================
# Uninstalling Packages
# =============================

# pip uninstall packagename

# =============================
# List of Packages
# =============================

# pip list

# =============================
# Show Package
# =============================

# pip show packagename

# =============================
# PIP Freeze
# =============================

# pip freeze

# =============================
# Reading from URL
# =============================

# pip install requests

import requests # importing the request module

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page

url = 'https://restcountries.eu/rest/v2/all'  # countries api

response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
countries = response.json()
print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries

# =============================
# Creating a Package
# =============================

# mypackage/arithmetics.py
# arithmetics.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

def subtract(a, b):
    return (a - b)

def multiple(a, b):
    return a * b

def division(a, b):
    return a / b

def remainder(a, b):
    return a % b

def power(a, b):
    return a ** b

# mypackage/greet.py
# greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'