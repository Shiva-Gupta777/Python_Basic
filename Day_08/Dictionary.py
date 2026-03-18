# Sum of values

data = {'a': 10, 'b': 20, 'c': 30}

total = sum(data.values())

print("Sum:", total)


# Common keys

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 4, 'c': 5, 'd': 6}

common = d1.keys() & d2.keys()  # & ka matlab hota hai intersection (common elements) 

print(common)


# Find key with max value

data = {'a': 10, 'b': 25, 'c': 15}

max_key = max(data, key=data.get)

print("Max key:", max_key)
print("Max value:", data[max_key])


# lets say i have list of L1  = [1,2,2,3,2,3,4,5] now identify the most repetivae element in the list

L1 = [1, 2, 2, 3, 2, 3, 4, 5]

freq = {}

# Step 1: Count frequency
for num in L1:           
    if num in freq:     #if number is already in frequency dictionary, then increment its count
        freq[num] += 1
    else:
        freq[num] = 1   #if number is not in frequency dictionary, then add it with count 1

# Step 2: Find max frequency element
max_element = max(freq, key=freq.get)

print("Most repetitive element:", max_element)



