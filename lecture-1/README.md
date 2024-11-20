## 1. Introduction to Python:

Python is a high-level, interpreted programming language known for its simplicity and readability.
It is widely used in web development, data analysis, artificial intelligence, scientific computing, and more.
Python code is written in plain text files with the extension .py and executed line by line (interpreted).


## 2. How Python Works:

Python uses an interpreter to convert your written code into instructions that a computer can understand.
This allows you to see results immediately, making it a great language for beginners.


## 3. The print() Function:

The print() function is used to display output on the screen.
#### Example:
print("Hello, World!")

#### Output:
Hello, World!

## 4. What Are Variables?

Variables are containers for storing data values.
You can think of a variable as a "label" for your data.
#### Example:
name = "Fariha"
age = 24
Here, name stores the string "Fariha", and age stores the integer 25.

## 5. Naming Variables:
### Rules for Naming Variables:
Must start with a letter or underscore (_).
Cannot start with a number.
Can only contain letters, numbers, and underscores.
Case-sensitive (name and Name are different).

#### Examples:
my_name = "Fariha"
age1 = 24
_temp = 98.6

#### Invalid Names:
2cool = "Nope"   (Starts with a number)
my-name = "Nope"  (Contains a hyphen)

## 6. Escape Sequences:
Escape sequences are special characters in Python strings that are preceded by a backslash (\) to perform specific actions.

### Common Escape Sequences:
Escape Sequence	       Meaning	                            Example
\n	                   Newline	                            "Hello\nWorld"
\t	                   Tab	                                "Hello\tWorld"
\\	                   Backslash	                        "This is a backslash: \\"
\'	                   Single quote inside a string	         'It\'s Python!'
\"	                   Double quote inside a string	         "He said, \"Hi!\""

#### Example:
print("Hello\nWorld")  # Adds a new line
print("He said, \"Python is awesome!\"")  # Includes double quotes in the string
Output:
Hello
World
He said, "Python is awesome!"

## 7. Single, Double, and Triple Quotes in Strings:
Python allows strings to be defined using single quotes ('), double quotes ("), or triple quotes (''' or """`).

### 7.1 Single Quotes (')
Used for simple strings without embedded quotes.
Example:
name = 'Fariha'
print(name)

### 7.2 Double Quotes (")
Allows inclusion of single quotes without using an escape sequence.
Example:
sentence = "It's a beautiful day!"
print(sentence)

### 7.3 Triple Quotes (''' or """)
Used for multi-line strings or strings that include both single and double quotes without escaping.
Example:
description = """This is a multi-line string.
It can span multiple lines and include both 'single' and "double" quotes."""
print(description)
Output:
This is a multi-line string.
It can span multiple lines and include both 'single' and "double" quotes.

### Key Notes:
Single (') and double (") quotes are interchangeable for single-line strings.
Triple quotes are ideal for docstrings or when dealing with multi-line text.
Escape sequences can be used in any type of quote.

## 8. What Are Data Types?
Data types define the kind of data a variable holds.

### Common Python Data Types:
String (str): Text data.
name = "Fariha"

Integer (int): Whole numbers.
age = 25

Float (float): Decimal numbers.
temperature = 36.6

Boolean (bool): True or False values.
is_student = True

List (list): A collection of items.
fruits = ["apple", "banana", "cherry"]

Dictionary (dict): Key-value pairs.
person = {"name": "Fariha", "age": 25}

Checking the Type of a Variable:
print(type(name))  
#### Output: 
<class 'str'>

## 9. Mutable vs Immutable Data Types:
In Python, data types can be categorized as mutable or immutable based on whether their value can be changed after they are created.

### Mutable Data Types:
Mutable objects can be modified after creation.
Examples: list, dict, set.
#### Example of a Mutable Type:
fruits = ["apple", "banana", "cherry"]
fruits[0] = "orange"  # Changing the first item
print(fruits)
#### Output:
['orange', 'banana', 'cherry']

### Immutable Data Types:
Immutable objects cannot be modified after creation.
Examples: int, float, str, tuple, frozenset.
#### Example of an Immutable Type:
name = "Fariha"
name[0] = "K"  # Trying to change the first letter will cause an error
#### Output:
TypeError: 'str' object does not support item assignment

### Key Differences Between Mutable and Immutable Types:
##### Feature	        Mutable	                          Immutable
    Modification	Can be changed in place	          Cannot be changed
    Examples	    list, dict, set	                  int, float, str, tuple
    Usage	        Suitable for dynamic content	  Suitable for fixed content




## Practice Question 1: Create and Print Variables with Different Data Types
## Task:

Create variables with the following data types:
A string containing the sentence: "Python's syntax is simple!"
An integer with the value 2024.
A float with the value 3.14.
A boolean indicating True.
Use the print() function to display each variable with its data type.

Solution:
##### Variables
text = "Python's syntax is simple!"  # String
year = 2024  # Integer
pi = 3.14  # Float
is_easy = True  # Boolean

##### Printing variables with their types
print("Text:", text, "- Type:", type(text))
print("Year:", year, "- Type:", type(year))
print("PI:", pi, "- Type:", type(pi))
print("Is Python Easy?", is_easy, "- Type:", type(is_easy))

##### Expected Output:
Text: Python's syntax is simple! - Type: <class 'str'>
Year: 2024 - Type: <class 'int'>
PI: 3.14 - Type: <class 'float'>
Is Python Easy? True - Type: <class 'bool'>

## Practice Question 2: Work with Escape Sequences and Quotes
## Task:

Use an escape sequence to print the following text, including quotes, on two lines:
Python says, "It's awesome!"
Keep learning.
Then, create a multi-line string using triple quotes with the same content.

Solution:
#### Using escape sequences
print("Python says, \"It's awesome!\"\nKeep learning.")

##### Using triple quotes
message = """Python says, "It's awesome!"
Keep learning."""
print(message)

#### Expected Output:
Python says, "It's awesome!"
Keep learning.
Python says, "It's awesome!"
Keep learning.