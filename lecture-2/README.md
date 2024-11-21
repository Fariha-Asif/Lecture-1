## String Functions:
### indexing: 
### index()
Purpose: It returns the index but through this we can't change the value of string.
Example:
text = "Python"
print(text[3])

text[0] = "F" # it will cause error
print(text)

### Slicing:
Purpose: It will return a specific piece of code from string.
#### Syntax:
string[start:end:step]

start: The index where the slicing begins (inclusive).
end: The index where the slicing ends (exclusive).
step: The interval at which characters are taken. Defaults to 1.

#### Examples
#### s1. Basic Slicing
Extracting a substring using start and end:
text = "Python Programming"
substring = text[0:6]  # Characters from index 0 to 5
print(substring)  # Output: Python

#### Explanation:
Start: 0 (starts at "P").
End: 6 (ends at index 5, "n").
The slice includes indices 0, 1, 2, 3, 4, 5.

#### 2. Omitting start or end:
When start or end is omitted, slicing defaults to the beginning or the end of the string.
text = "Python Programming"
print(text[:6])   # Output: Python (from start to index 5)
print(text[7:])   # Output: Programming (from index 7 to the end)

#### 3. Using step
The step parameter controls how many characters to skip.
text = "Python Programming"
print(text[0:10:2])  # Output: Pto rg

#### Explanation:
Start: 0 (starts at "P").
End: 10 (ends at index 9, "g").
Step: 2 (takes every second character).

#### 4. Negative Indices:
You can use negative indices to slice from the end of the string.
text = "Python Programming"
print(text[-11:-1])  # Output: Programmin

#### Explanation:
Start: -11 (11th character from the end).
End: -1 (excludes the last character).

#### 5. Reversing a String
A negative step reverses the order of the characters.
text = "Python"
print(text[::-1])  # Output: nohtyP

#### Explanation:
Start: Omitted (defaults to the end of the string).
End: Omitted (defaults to the start of the string).
Step: -1 (reverses the string).

### 1. len()
Purpose: Returns the length (number of characters) in a string.
Example:
text = "Hello, World!"
print(len(text))  # Output: 13

### 2. lower()
Purpose: Converts all characters in the string to lowercase.
Example:
text = "PYTHON"
print(text.lower())  # Output: python

### 3. upper()
Purpose: Converts all characters in the string to uppercase.
Example:
text = "python"
print(text.upper())  # Output: PYTHON

### 4. strip()
Purpose: Removes leading and trailing whitespace.
Example:
text = "   Hello   "
print(text.strip())  # Output: Hello

### 5. replace()
Purpose: Replaces a substring with another substring in the string.
Example:
text = "Hello, World!"
print(text.replace("World", "Python"))  # Output: Hello, Python!

### 6. split()
Purpose: Splits a string into a list based on a specified delimiter.
Example:
text = "apple,banana,cherry"
print(text.split(","))  # Output: ['apple', 'banana', 'cherry']

### 7. find()
Purpose: Returns the index of the first occurrence of a substring. Returns -1 if not found.
Example:
text = "Hello, World!"
print(text.find("World"))  # Output: 7

### 8. startswith()
Purpose: Checks if a string starts with a specified substring.
Example:
text = "Python is fun"
print(text.startswith("Python"))  # Output: True

### 9. endswith()
Purpose: Checks if a string ends with a specified substring.
Example:
text = "Learning Python"
print(text.endswith("Python"))  # Output: True

### 10. capitalize()
Purpose: Capitalizes the first character of the string and makes the rest lowercase.
Example:
text = "python is fun"
print(text.capitalize())  # Output: Python is fun

### 11. title()
Purpose: Converts the first character of each word to uppercase.
Example:
text = "learning python is fun"
print(text.title())  # Output: Learning Python Is Fun

### 12. islower()
Purpose: Checks if all characters in the string are lowercase.
Example:
text = "python"
print(text.islower())  # Output: True

### 13. isupper()
Purpose: Checks if all characters in the string are uppercase.
Example:
text = "PYTHON"
print(text.isupper())  # Output: True

### 14. isalpha()
Purpose: Checks if the string contains only alphabetic characters (no spaces or numbers).
Example:
text = "Python"
print(text.isalpha())  # Output: True

### 15. isdigit()
Purpose: Checks if the string contains only digits.
Example:
text = "12345"
print(text.isdigit())  # Output: True

### 16. isalnum()
Purpose: Checks if the string contains only alphanumeric characters (letters and numbers).
Example:
text = "Python123"
print(text.isalnum())  # Output: True

### 17. swapcase()
Purpose: Swaps the case of all characters in the string.
Example:
text = "PyThOn"
print(text.swapcase())  # Output: pYtHoN

### 18. join()
Purpose: Joins elements of an iterable into a single string, separated by the string it's called on.
Example:
words = ["Python", "is", "fun"]
print(" ".join(words))  # Output: Python is fun

### 19. Expandtabs()
Purpose: Adjust Tab spaces as you want
text = "I love coding. \t Coding is my passion."
print(text.expandtabs(10))

### 20. center()
Purpose: Adjust text in center
text = "I love Coding."
print(text.center(20))

how it works:
(width - total length of string) / 2
(20 - 13) / 2

## List Functions:

### 1. append()
Purpose: Adds an element to the end of the list.
Example:
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

### 2. insert()
Purpose: Inserts an element at a specified position.
Example:
fruits = ["apple", "banana"]
fruits.insert(1, "cherry")
print(fruits)  # Output: ['apple', 'cherry', 'banana']

### 3. remove()
Purpose: Removes the first occurrence of an element.
Example:
fruits = ["apple", "banana", "apple"]
fruits.remove("apple")
print(fruits)  # Output: ['banana', 'apple']

### 4. pop()
Purpose: Removes and returns an element at a specified index. Defaults to the last element if no index is provided.
Example:
fruits = ["apple", "banana", "cherry"]
print(fruits.pop(1))  # Output: banana
print(fruits)  # Output: ['apple', 'cherry']

### 5. sort()
Purpose: Sorts the list in ascending order.
Example:
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5]

### 6. reverse()
Purpose: Reverses the order of the list.
Example:
numbers = [1, 2, 3]
numbers.reverse()
print(numbers)  # Output: [3, 2, 1]

### 7. index()
Purpose: Returns the index of the first occurrence of a specified element.
Example:
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # Output: 1

### 8. count()
Purpose: Returns the number of times an element appears in the list.
Example:
fruits = ["apple", "banana", "apple"]
print(fruits.count("apple"))  # Output: 2

### 9. extend()
Purpose: Adds all elements of an iterable to the end of the list.
Example:
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date'];