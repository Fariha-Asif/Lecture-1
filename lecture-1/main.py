print("Fariha Faraz")


# variable   value
name = "Fariha"
print(name)

age = 24
print(age)

# Naming Variable:

my_name = "Fariha"
print(my_name)

age1 = 24
print(age1)

_temp = 98.6
print(_temp)

# Invalid Variable:
# 2cool = "Nope"   (Starts with a number)
# my-name = "Nope"  (Contains a hyphen)

# Escape Sequence:

# Common Escape Sequences:
# Escape Sequence	       Meaning	                            Example
# \n	                   Newline	                            "Hello\nWorld"
# \t	                   Tab	                                "Hello\tWorld"
# \\	                   Backslash	                        "This is a backslash: \\"
# \'	                   Single quote inside a string	         'It\'s Python!'
# \"	                   Double quote inside a string	         "He said, \"Hi!\""

print("Hello\nWorld")  # Adds a new line
print("Hello\tWorld")
print("This is a backslash: \\")
print('It\'s Python!')
print("He said, \"Hi!\"")

# Single Quote:
name = 'Fariha'
print(name)
print("My name is 'Fariha'")

# Double Quote:
name = "Fariha"
print(name)
print('My name is "Fariha"')

# Tripple Quotes:
name = """Fariha"""
print(name)
print("""My name is "Fariha".
      I am 24 years old
      I live in 'Karachi'.""")

# Data Types:
# String (str): Text data.
name = "Fariha"
print(name)
print(type(name))

# Integer (int): Whole numbers.
age = 24
print(age)
print(type(age))

# Float (float): Decimal numbers.
temperature = 36.6
print(temperature)
print(type(temperature))

# Boolean (bool): True or False values.
is_student = True
print(is_student)
print(type(is_student))

# List (list): A collection of items.
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(type(fruits))


roll_numbers = [123, 234, 132, 232]
print(roll_numbers)
print(type(roll_numbers))

# Dictionary (dict): Key-value pairs.
# var =    key  :  value  , key-2: value
person = {"name": "Fariha", "age": 25}
print(person)
print(type(person))


# Mutable & Immutable:
# Mutable objects can be modified after creation.
# Examples: list, dict, set.
# index =   0        1         2
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits[0] = "orange"  # Changing the first item
print(fruits)

person = {"name": "Fariha", "age": 25}
print(person)
person["name"] = "Faraz"
print(person)

# Immutable objects cannot be modified after creation.
# Examples: int, float, str, tuple, frozenset.
name = "Fariha"
name[0] = "K"
print(name)

# Practice Question 1:


# Create variables with the following data types:
# A string containing the sentence: "Python's syntax is simple!"
# An integer with the value 2024.
# A float with the value 3.14.
# A boolean indicating True.
# Use the print() function to display each variable with its data type.


# Practice Question 2:

# Use an escape sequence to print the following text, including quotes, on two lines:
# Python says, "It's awesome!"
# Keep learning.

# Then, create a multi-line string using triple quotes with the same content.

