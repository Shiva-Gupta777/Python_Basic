# Question: Create a list of 5 fruits and print the list

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print(fruits)


# Question: Create a list of numbers and print the first and last element

numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])
print("Last element:", numbers[-1])


# Question: Create a list of 3 colors and add one more color using append()

colors = ["Red", "Blue", "Green"]

colors.append("Yellow")

print(colors)



# Question: Insert a new number at index position 2

numbers = [1, 2, 4, 5]

numbers.insert(2, 3)

print(numbers)


# Question: Remove "Mango" from the list

fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits.remove("Mango")

print(fruits)


# Question: Print all elements of a list using for loop

numbers = [5, 10, 15, 20, 25]

for num in numbers:
    print(num)


# Question: Find how many elements are in the list

students = ["Rahul", "Aman", "Riya", "Shiva"]

print("Total students:", len(students))


# Question: Check if "Python" exists in the list

languages = ["Java", "C", "Python", "JavaScript"]

if "Python" in languages:
    print("Python is present")
else:
    print("Python is not present")


# Question: Sort a list of numbers

numbers = [50, 10, 30, 20, 40]

numbers.sort()

print(numbers)



# Question: Reverse the list

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)


# Question: Find the largest number in a list

numbers = [10, 25, 5, 70, 30]

max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print("Largest number is:", max_num)


# Question: Find the smallest number in a list

numbers = [10, 25, 5, 70, 30]

min_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num

print("Smallest number is:", min_num)




# Question: Calculate the sum of all elements in a list

numbers = [10, 20, 30, 40]

total = 0

for num in numbers:
    total = total + num

print("Sum of elements:", total)


# Question: Find the average of numbers in a list

numbers = [10, 20, 30, 40]

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print("Average:", average)




# Question: Count how many even numbers are in the list

numbers = [1, 2, 3, 4, 5, 6]

count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print("Total even numbers:", count)



# Question: Reverse a list without using built-in function

numbers = [1, 2, 3, 4, 5]

reversed_list = []

for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed list:", reversed_list)



# Question: Find the second largest number in a list

numbers = [10, 50, 20, 40, 30]

numbers.sort()

print("Second largest:", numbers[-2])


# Question: Check whether a number exists in the list

numbers = [5, 10, 15, 20]

search = 15

if search in numbers:
    print("Number found")
else:
    print("Number not found")


# Question: Merge two lists into one

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = list1 + list2

print("Merged list:", merged_list)


# Question: Remove duplicate elements from a list

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("List without duplicates:", unique_list)