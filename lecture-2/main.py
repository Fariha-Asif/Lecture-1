# String Method:

# Indexing:
#       0 1 2 3 4 5
text = "Python" # By default indexing starts from 0
print(text[3])
print(text[0])

text[0] = "F" # it will cause error
print(text)

# string[start:end:step]

# Basic Slicing:

text = "Python Programming"
substring = text[0:6]  # Characters from index 0 to 5
print(substring)  # Output: Python

### 2. Omitting start or end:
# When start or end is omitted, slicing defaults to the beginning or the end of the string.
text = "Python Programming"
print(text[:6])   # Output: Python (from start to index 5)
print(text[7:])   # Output: Programming (from index 7 to the end)

### 3. Using step
# The step parameter controls how many characters to skip.
text = "Python Programming"
#         start: End: Step
print(text[0:10:2])  # Output: Pto rg

# Negative Indexing in slicing:
# You can use negative indices to slice from the end of the string.
#              -4 -3 -2 -1
text = "Python Programming"
print(text[-11:-1])  # Output: Programmin

# Reversing string:
text = "Python"
print(text[::-1])  # Output: nohtyP

# Length:

text = "Hello, World!"
print(len(text))  # Output: 13

text = "PYTHON"
print(text.lower())

text = "python"
print(text.upper())  # Output: PYTHON

text = "   Hello   "
print(text)
print(text.strip())  # Output: Hello

text = "Hello, World!"
print(text)
print(text.replace("World", "Python"))  # Output: Hello, Python!

text = "apple,banana,cherry"
print(text.split(","))  # Output: ['apple', 'banana', 'cherry']

text = "Hello, World!"
print(text.find("World"))  # Output: 7

text = "Python is fun"
print(text.startswith("Python"))  # Output: True
print(text.startswith("World"))

text = "Learning Python"
# print(text.endswith("Python"))  # Output: True
print(text.endswith("World"))

text = "python is fun"
print(text.capitalize())  # Output: Python is fun

text = "learning python is fun"
print(text.title())  # Output: Learning Python Is Fun

text = "python"
print(text.islower())  # Output: True

text = "Python"
print(text.isupper())  # Output: True

text = "PyThOn"
print(text.swapcase())  # Output: pYtHoN

words = ["Python", "is", "fun"]
print(" ".join(words))  # Output: Python is fun

text = "I love coding. \t Coding is my passion."
print(text)
print(text.expandtabs(20))

text = "I love Coding."
print(text.center(20))

# (width - total length of string) / 2
# (20 - 13) / 2 = 7/2 

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

fruits = ["apple", "banana"]
fruits.insert(1, "cherry")
print(fruits)  # Output: ['apple', 'cherry', 'banana']

fruits = ["apple", "banana", "apple"]
fruits.remove("apple")
print(fruits)  # Output: ['banana', 'apple']

fruits = ["apple", "banana", "cherry"]
print(fruits.pop(1))  # Output: banana
print(fruits)  # Output: ['apple', 'cherry']

numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5]

numbers = [1, 2, 3]
numbers.reverse()
print(numbers)  # Output: [3, 2, 1]

fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # Output: 1

fruits = ["apple", "banana", "apple"]
print(fruits.count("apple"))  # Output: 2

fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date'];
