# =============================
# Exercises: Level 1
# =============================

import math
from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count())

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def mode(self):
        counts = Counter(self.data)
        mode_value = counts.most_common(1)[0]
        return mode_value  # (value, frequency)

    def var(self):
        mean = self.mean()
        return round(sum((x - mean) ** 2 for x in self.data) / self.count(), 1)

    def std(self):
        return round(math.sqrt(self.var()), 1)

    def freq_dist(self):
        counts = Counter(self.data)
        total = self.count()
        return [(round((count / total) * 100, 1), value) for value, count in counts.items()]

    def describe(self):
        print("Count:", self.count())
        print("Sum:", self.sum())
        print("Min:", self.min())
        print("Max:", self.max())
        print("Range:", self.range())
        print("Mean:", self.mean())
        print("Median:", self.median())
        print("Mode:", self.mode())
        print("Variance:", self.var())
        print("Standard Deviation:", self.std())
        print("Frequency Distribution:", self.freq_dist())


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24,
        32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
data.describe()

# =============================
# Exercises: Level 2
# =============================


class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def add_income(self, description, amount):
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        self.expenses[description] = amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return f"{self.firstname} {self.lastname}"


account = PersonAccount("Hugo", "Frias")

account.add_income("Salary", 3000)
account.add_income("Freelance", 1200)

account.add_expense("Rent", 1200)
account.add_expense("Food", 500)

print("Account Owner:", account.account_info())
print("Total Income:", account.total_income())
print("Total Expenses:", account.total_expense())
print("Balance:", account.account_balance())
