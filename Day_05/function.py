# Question: Create a function that prints "Hello Python"

def greet():
    print("Hello Python")

greet()


# Question: Create a function that takes a name as parameter and prints greeting

def greet(name):
    print("Hello", name)

greet("Shiva")



# Question: Create a function that returns the sum of two numbers

def add(a, b):
    result = a + b
    return result

answer = add(5, 7)

print("Sum is:", answer)


# Question: Write a function to check whether a number is even or odd

def check_even_odd(num):

    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

check_even_odd(10)


# Question: Write a function that finds the largest of three numbers

def largest(a, b, c):

    if a > b and a > c:
        print("Largest:", a)

    elif b > c:
        print("Largest:", b)

    else:
        print("Largest:", c)

largest(10, 20, 15)



# Question: Write a function to calculate factorial of a number
     #The factorial of a number is the product of all positive integers from that number down to 1.
 
def factorial(n):

    result = 1

    for i in range(1, n+1):
        result = result * i

    return result

print("Factorial:", factorial(5))


# Question: Write a function that finds the maximum number in a list

def find_max(numbers):

    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num

numbers = [10,50,20,40]

print("Maximum number:", find_max(numbers))


# Question: Create a function with default parameter

def greet(name="Guest"):
    print("Hello", name)

greet("Shiva")
greet()



# Question: Write a function to reverse a string

def reverse_string(text):

    reversed_text = text[::-1]

    return reversed_text

print(reverse_string("Python"))

# #see this is structure of slicing text[start : end : step]  like text[0:4:1] so simply  we use in this example  ::-1 means start = blank (means start automatically)
# end = blank (means go till end)
# step = -1  Step = -1 ka matlab hai reverse direction me chalna.



# Question: Create a function that counts elements in a list

def count_elements(my_list):

    count = 0

    for item in my_list:
        count += 1

    return count

numbers = [10,20,30,40]

print("Total elements:", count_elements(numbers))
