# Conditional Statement in Python
# Definition: A conditional statement is used to make decisions in a program based on a condition (True or False).

# Example 1: Simple if statement
age = 18

if age >= 18:
    print("You are eligible to vote")


# Example 2: if-else statement
number = 10

if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


# Example 3: if-elif-else statement
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# Example 4: Checking positive, negative or zero
num = -5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")