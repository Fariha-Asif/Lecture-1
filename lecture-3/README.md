## Opertors in Python:
### A. Arithmetic Operators
#### Operator	Description	        Example
        +	    Addition	        3 + 2 = 5
        -	    Subtraction	        5 - 2 = 3
        *	    Multiplication	    4 * 2 = 8
        /	    Division	        10 / 2 = 5.0
        //	    Floor Division	    10 // 3 = 3
        %	    Modulus (Remainder)	10 % 3 = 1
        **	    Exponentiation	    2 ** 3 = 8


### B. Comparison Operators
####   Operator	Description	            Example
        ==	    Equal to	            5 == 5 → True
        !=	    Not equal to            5 != 3 → True
        >	    Greater than            5 > 3 → True
        <	    Less than	            3 < 5 → True
        >=	    Greater than or equal   5 >= 5 → True
        <=	    Less than or equal	    4 <= 5 → True

### C. Logical Operators
####    Operator	Description	                                      Example
        and	       Returns True if both conditions are True	        (5 > 3) and (4 > 2) → True
        or	       Returns True if at least one condition is True	(5 > 3) or (2 > 4) → True
        not	       Reverses the logical value	                 not (5 > 3) → False

        
### D. Assignment Operators
####     Operator	Description	       Example
            =	    Assigns value	        x = 10
            +=      Adds and assigns	        x += 5 → x = x + 5
            -=	    Subtracts and assigns	x -= 5 → x = x - 5
            *=	    Multiplies and assigns	x *= 5 → x = x * 5
            /=	    Divides and assigns	        x /= 5 → x = x / 5

### E. Membership Operators
####    Operator	Description	                    Example
          in	    Returns True if value is found	'a' in 'apple' → True
        not in	    Returns True if value is absent	'x' not in 'apple' → True

## Introduction to Conditional Statements
### What are Conditional Statements?
Conditional statements allow programs to make decisions and execute specific code based on conditions.
### Why are they important?
They enable dynamic program behavior by reacting to different inputs or situations.
### 2. Types of Conditional Statements
#### a. if Statement
Executes a block of code if a specified condition is True.
Example:
age = 18
if age >= 18:
    print("You are eligible to vote.")

#### b. if-else Statement
Provides an alternative block of code if the condition is False.
Example:
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#### c. if-elif-else Statement
Checks multiple conditions in sequence.
Example:
light = "green"

if light == "red":
    print("Stop")
elif light == "green":
    print("Go")
elif light == "Yellow":
    print("Wait")
else:
    print("Light is Broken")

#### d. Nested if Statements
Allows conditions inside another if block.
Example:
number = 15
if number > 10:
    if number % 2 == 0:
        print("Even and greater than 10")
    else:
        print("Odd and greater than 10")

age = 34
if(age >= 18):
    if(age >= 80):
        print("Cannot drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")

    

##### Practice Question:

###### Question 1: Grade Checker
Write a program to assign grades based on marks using conditional statements.

marks = int(input("Enter your marks: "))
if marks >= 90:
    grade = "A+"
elif marks >= 80 and marks < 90:
    grade = "A"
elif marks >= 70 and marks < 80:
    grade = "B"
elif marks >= 60 and marks < 70:
    grade = "C"
else:
    grade = "D"

print("Your grade is:", grade)

##### Question 2: Number Checker
Write a program to check whether a number is positive, negative, or zero.

number = int(input("Enter a number: "))
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")