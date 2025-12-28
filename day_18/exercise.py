# =============================
# Exercises: Level 1
# =============================

# 1. What is the most frequent word in the following paragraph?

paragraph = (
    "I love teaching. If you do not love teaching what else can you love. "
    "I love Python if you do not love something which can give you all the "
    "capabilities to develop an application what else can you love."
)

import re
from collections import Counter

def most_frequent_words(text):
    words = re.findall(r'\b\w+\b', text)
    counts = Counter(words)
    return counts.most_common()

print(most_frequent_words(paragraph))


# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) # 20

numbers = list(map(int, points))
distance = max(numbers) - min(numbers)

print(distance)

# =============================
# Exercises: Level 2
# =============================

# 1. Write a pattern which identifies if a string is a valid python variable

def is_valid_variable(name):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, name))

print(is_valid_variable('first_name'))   # True
print(is_valid_variable('first-name'))   # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))    # True

# =============================
# Exercises: Level 3
# =============================

# 1. Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    cleaned = re.sub(r'[^a-zA-Z\s]', '', text)
    return re.sub(r'\s+', ' ', cleaned).strip()

cleaned_text = clean_text(sentence)
print(cleaned_text)

from collections import Counter

def most_frequent_words(text, n=3):
    words = text.split()
    counts = Counter(words)
    return counts.most_common(n)

print(most_frequent_words(cleaned_text))