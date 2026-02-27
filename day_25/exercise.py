import pandas as pd

# Read the hacker_news.csv file from data directory
df = pd.read_csv("hacker_news.csv")

# Display basic info
print(df.head())

# Get the first five rows
df.head()

# Get the last five rows
df.tail()

# Get the title column as pandas series
titles = df['title']
print(titles)
print(type(titles))

# Count the number of rows and columns
rows, columns = df.shape
print("Rows:", rows)
print("Columns:", columns)

df.shape

# Filter the titles which contain python
python_titles = df[df['title'].str.contains('python', case=False, na=False)]

print(python_titles[['title']])
print("Total Python titles:", len(python_titles))

# Filter the titles which contain JavaScript
js_titles = df[df['title'].str.contains('javascript', case=False, na=False)]

print(js_titles[['title']])
print("Total JavaScript titles:", len(js_titles))

# Explore the data and make sense of it
df.info()