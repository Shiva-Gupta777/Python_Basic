# Question: Remove duplicates from a list

nums = [1, 2, 2, 3, 4, 4]

unique = set(nums)

print(unique)


# Question: Find union of two sets

a = {1, 2, 3}
b = {3, 4, 5}

result = a | b

print(result)


# Question: Find common elements between two sets

a = {1, 2, 3}
b = {2, 3, 4}

result = a & b

print(result)


# Question: Find elements present in a but not in b

a = {1, 2, 3}
b = {2, 3, 4}

result = a - b

print(result)

# Question: Check if element 5 exists in set

s = {1, 2, 3, 4}

if 5 in s:
    print("Found")
else:
    print("Not Found")



# Question: Add and remove elements

s = {1, 2, 3}

s.add(4)      # add
s.remove(2)   # remove

print(s)


# Question: Find number of elements in set

s = {1, 2, 3, 4}

print(len(s))


# Question: Convert set to list

s = {1, 2, 3}

lst = list(s)

print(lst)


# Question: Check if a is subset of b

a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))

# Question: Remove all elements from set

s = {1, 2, 3}

s.clear()

print(s)