# Q7. Write a Python program to convert a given list of strings and characters to a single list of
# characters.

words = ["apple", "banana", "orange", "grapes","grapes","banana"]
e_lst = []

for word in words:
    for ch in word:
        e_lst.append(ch)

print(e_lst)

# More Pythonic Solution

words = ["apple", "banana", "orange", "grapes","grapes","banana"]

result = [ch for word in words for ch in word]

print(result)

# Using extend()

words = ["apple", "banana", "orange", "grapes", "grapes", "banana"]

e_lst = []

for word in words:
    e_lst.extend(word)
print(e_lst)