# =============================
# Exercises: Level 1
# =============================

# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words
def count_lines_and_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        words = sum(len(line.split()) for line in lines)
    return len(lines), words

files = [
    './data/obama_speech.txt',
    './data/michelle_obama_speech.txt',
    './data/donald_speech.txt',
    './data/melina_trump_speech.txt'
]

for file in files:
    lines, words = count_lines_and_words(file)
    print(f"{file}: {lines} lines, {words} words")

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json
from collections import Counter

def most_spoken_languages(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)

    languages = []
    for country in countries:
        languages.extend(country.get('languages', []))

    counts = Counter(languages)
    return [(count, lang) for lang, count in counts.most_common(top_n)]

# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def most_populated_countries(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)

    sorted_countries = sorted(
        countries,
        key=lambda c: c['population'],
        reverse=True
    )

    return [
        {'country': c['name'], 'population': c['population']}
        for c in sorted_countries[:top_n]
    ]

print(most_populated_countries('./data/countries_data.json', 10))
print(most_populated_countries('./data/countries_data.json', 3))

# =============================
# Exercises: Level 2
# =============================

# 1. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re

def extract_emails(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)

# 2. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
def find_most_common_words(source, top_n):
    import re
    from collections import Counter

    if source.endswith('.txt'):
        with open(source, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        text = source

    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    counts = Counter(words)
    return [(count, word) for word, count in counts.most_common(top_n)]

# 3. Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
speeches = [
    './data/obama_speech.txt',
    './data/michelle_obama_speech.txt',
    './data/donald_speech.txt',
    './data/melina_trump_speech.txt'
]

for speech in speeches:
    print(speech)
    print(find_most_common_words(speech, 10))

# 4. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory

# TODO

# 6. Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript
import csv

def count_hacker_news(filename):
    python = javascript = java = 0

    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            title = row[1].lower()
            if 'python' in title:
                python += 1
            if 'javascript' in title:
                javascript += 1
            if 'java' in title and 'javascript' not in title:
                java += 1

    return python, javascript, java

print(count_hacker_news('./data/hacker_news.csv'))