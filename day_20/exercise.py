
import requests
import re
from collections import Counter
import statistics
import requests
from bs4 import BeautifulSoup

# 1 . Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

def most_frequent_words_from_url(url, n=10):
    response = requests.get(url)
    text = response.text.lower()
    words = re.findall(r'\b[a-z]+\b', text)
    return Counter(words).most_common(n)

print(most_frequent_words_from_url(romeo_and_juliet, 10))

# 2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
cats_api = 'https://api.thecatapi.com/v1/breeds'
cats = requests.get(cats_api).json()

# the min, max, mean, median, standard deviation of cats' weight in metric units.
weights = []

for cat in cats:
    weight = cat['weight']['metric']
    min_w, max_w = map(int, weight.split(' - '))
    weights.extend([min_w, max_w])

print("Weight statistics:")
print("Min:", min(weights))
print("Max:", max(weights))
print("Mean:", statistics.mean(weights))
print("Median:", statistics.median(weights))
print("Std Dev:", statistics.stdev(weights))

# the min, max, mean, median, standard deviation of cats' lifespan in years.
lifespans = []

for cat in cats:
    life = cat['life_span']
    min_l, max_l = map(int, life.split(' - '))
    lifespans.extend([min_l, max_l])

print("\nLifespan statistics:")
print("Min:", min(lifespans))
print("Max:", max(lifespans))
print("Mean:", statistics.mean(lifespans))
print("Median:", statistics.median(lifespans))
print("Std Dev:", statistics.stdev(lifespans))

# Create a frequency table of country and breed of cats
countries = Counter()
breeds = Counter()

for cat in cats:
    if cat.get('origin'):
        countries[cat['origin']] += 1
    breeds[cat['name']] += 1

print("Countries frequency:", countries)
print("Breeds frequency:", breeds)

# 3. Read the countries API and find
countries_api = 'https://restcountries.com/v3.1/all'
countries = requests.get(countries_api).json()

# the 10 largest countries
# TODO

# the 10 most spoken languages
languages = []

for country in countries:
    if 'languages' in country:
        languages.extend(country['languages'].values())

lang_freq = Counter(languages).most_common(10)
print(lang_freq)

# the total number of languages in the countries API
unique_languages = set(languages)
print("Total languages:", len(unique_languages))

# 4. UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
uci_url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(uci_url)
soup = BeautifulSoup(response.text, 'html.parser')

datasets = soup.find_all('a')

uci_datasets = [
    d.text.strip()
    for d in datasets
    if d.get('href') and 'datasets' in d.get('href')
]

print("Number of datasets:", len(uci_datasets))
print("Sample datasets:", uci_datasets[:10])