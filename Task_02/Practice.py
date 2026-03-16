# Project Overview: Create a simple calculator that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division. Each operation will be implemented as a separate function, and the user can choose which operation to perform. add(a, b) for addition subtract(a, b) for subtraction multiply(a, b) for multiplication divide(a, b) for division


# function for addition
def add(a, b):
    return a + b


# function for subtraction
def subtract(a, b):
    return a - b


# function for multiplication
def multiply(a, b):
    return a * b


# function for division
def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b


# user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice == "1":
    print("Result:", add(num1, num2))

elif choice == "2":
    print("Result:", subtract(num1, num2))

elif choice == "3":
    print("Result:", multiply(num1, num2))

elif choice == "4":
    print("Result:", divide(num1, num2))

else:
    print("Invalid choice")