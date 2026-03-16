# Question: Create a file and write some text into it

file = open("data.txt", "w")

file.write("Hello Python\n")
file.write("File handling practice")

file.close()



# Question: Read the content of a file

file = open("data.txt", "r")

content = file.read()

print(content)

file.close()


# Question: Read file line by line

file = open("data.txt", "r")

for line in file:
    print(line)

file.close()


# Question: Add new text to existing file

file = open("data.txt", "a")

file.write("\nLearning Python")

file.close()


# Question: Check if file exists

import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File not found")