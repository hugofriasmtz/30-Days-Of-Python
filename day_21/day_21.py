# Creating a Class
class Person:
  pass
print(Person)

# Creating an Object
p = Person()
print(p)

# Class Constructor
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city


p = Person('Hugo', 'Frias', 22, 'Mexico', 'Queretaro')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)

# Object Methods
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Marcos', 'Frias', 28, 'Mexico', 'Puebla')
print(p.person_info())

# Object Default Methods
class Person:
      def __init__(self, firstname='Erwin', lastname='Frias', age=31, country='Mexico', city='Puebla'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('Karen', 'Jimenez', 2, 'BR', 'Puerto Alegria')
print(p2.person_info())

# Method to Modify Class Default Values
class Person:
      def __init__(self, firstname='Felipe', lastname='Frias', age=51, country='Mexico', city='CDMX'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
print(p1.skills)
p2 = Person('Marcos', 'Frias', 28, 'Mexico', 'Nuevo Leon')
print(p2.person_info())
p2.add_skill('PHP')
print(p2.skills)

# Inheritance
class Student(Person):
    pass

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

# Overriding parent method
class Student(Person):
    def __init__ (self, firstname='Hugo', lastname='Frias',age=22, country='Mexico', city='Queretaro', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)
    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student()
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)