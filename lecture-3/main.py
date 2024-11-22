# Operators:
# Arithmetic operators:
# Adding:
print(3 + 5)
a = 3
b = 5
print(a + b)

# Subtraction:
print(4 - 2)

# # Multiplication:
print(2 * 2)

# Division:
print(4 / 2)

# Floor Division:
print(10 // 3) # output 3.33  

# Modulus (Remainder)
print(15 % 2)

# Exponentiation (power)
print(2 ** 3) # output 8

# Comparision Operators:

# Equal to: ==

a = 5
b = 3
print(a == b) #output False

# Not Equal to:
print(a != b) # output True

# # Greater Than:
print(a > b) #output False

# Less than:
print(a < b) # output False

# Greater than or equals to:
print(a >= b) # output True

# Less than or equals to:
print(a <= b) # output True

#  Logical Operators:
# and 
print(5 < 3) and (1 > 4) #output False
# or 
print((5 > 3) or (2 > 4)) #output True
# not
print(not (5 < 3))

# Assignment Operators:
# Assigns value:
x = 10
print(x)
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 2
print(x)

# Membership Operators
# in
fruit = "apple"
print('a' in 'apple') # output True

# not in
print('a' not in 'apple')

# Conditional Statement:
# if statement:
age = 16
if age >= 18:
    print("You are eligible to make CNIC")


if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

traffic_light = "grey"

if traffic_light == "red":
    print("Stop")
elif traffic_light == "green":
    print("Go")
elif traffic_light == "Yellow":
    print("Wait")
else:
    print("light has been broken.")

# Nested if statement:
number = 7
if number > 10:
    if number % 2 == 0:
        print("Even and greater than 10")
    else:
        print("Odd and greater than 10")
else:
    print("Number should be greater than 10")

age = 16
if(age >= 18):
    if(age >= 80):
        print("Cannot drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")

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

number = int(input("Enter a number: "))
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")





