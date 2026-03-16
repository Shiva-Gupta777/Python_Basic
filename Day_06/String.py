# Question: Reverse a string

text = "python"

print(text[::-1])


# Question: Check if a string is palindrome

text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")



# Question: Count vowels in a string

text = "python programming"

vowels = "aeiou"

count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Total vowels:", count)



# Question: Count consonants in a string

text = "python"

vowels = "aeiou"

count = 0

for ch in text:
    if ch.isalpha() and ch not in vowels:   #Python string method that checks whether a character is an alphabet letter.
        count += 1

print("Consonants:", count)


# Question: Count number of words in a sentence

sentence = "Python is easy to learn"
 
words = sentence.split()     #to break a string into a list of words.

print("Total words:", len(words))


# Question: Remove spaces from string

text = "Python is easy"

print(text.replace(" ", ""))


# Question: Find length of string

text = "Python"

print(len(text))


# Question: Count frequency of characters in string 
      #In a given string, find how many times each character appears.
      #{'b':1, 'a':3, 'n':2}

text = "banana"

freq = {}   # This dictionary will store:

for ch in text:    #Loop reads characters one by one:
    if ch in freq:   #If the character is already in the dictionary.
        freq[ch] += 1    #If the character is already in the dictionary, its count is incremented by 1.
    else:
        freq[ch] = 1    #If the character is not in the dictionary, it is added with a count of 1.

print(freq)


# Question: Check if string contains digit

text = "python123"

for ch in text:
    if ch.isdigit():
        print("Digit found")
        break



# Question: Remove duplicate characters

text = "programming"

result = ""

for ch in text:
    if ch not in result:
        result += ch

print(result)

# Question: Find longest word in sentence

sentence = "Python programming is very powerful"

words = sentence.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)



# Question: Replace a word in string

text = "Python is easy"

new_text = text.replace("easy", "awesome")

print(new_text)



# Question: Check if string starts with 'P'

text = "Python"

if text.startswith("P"):
    print("Yes, starts with P")
else:
    print("No")