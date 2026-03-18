# Question: Find Maximum and Minimum in a Tuple

t = (10, 5, 20, 8)

print("Max:", max(t))
print("Min:", min(t))

# Question: Count Frequency of Elements in a Tuple

t = (1, 2, 2, 3, 1, 4)

freq = {}

for i in t:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

# Question: Remove Duplicates from a Tuple

t = (1, 2, 2, 3, 4, 4)

unique = tuple(set(t))

print(unique)


# Question: Find Sum of Elements in a Tuple

t = (1, 2, 3, 4)

total = sum(t)

print(total)


# Question: Check if Element Exists in Tuple

t = (1, 2, 3, 4)

if 5 in t:
    print("Found")
else:
    print("Not Found")


# Question: Find Common Elements in Two Tuples

t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)

common = tuple(set(t1) & set(t2))

print(common)


# Question: Flatten a Nested Tuple  (doubt)

t = (1, (2, 3), (4, 5))

result = ()

for i in t:
    if isinstance(i, tuple):
        result += i
    else:
        result += (i,)
print(result)


# Question: Sort a Tuple

t = (4, 1, 3, 2)

sorted_t = tuple(sorted(t))

print(sorted_t)



# Question: Swap First and Last Elements of Tuple

t = (1, 2, 3, 4)

lst = list(t)

lst[0], lst[-1] = lst[-1], lst[0]

t = tuple(lst)

print(t)