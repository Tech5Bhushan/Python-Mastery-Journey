# Q3. Write a Python program to split a list based on first character of word.

words = ["apple", "ant", "banana", "ball", "cat", "car"]

result ={}

for word in words:
    first_char =word[0]

    if first_char not in result:
        result[first_char] = []

    result[first_char].append(word)

print(result)

# Using defaultdict (Pythonic)

from collections import defaultdict

words = ["apple", "ant", "banana", "ball", "cat", "car"]

result = defaultdict(list)

for word in words:
    result[word[0]].append(word)

print(dict(result))

# Best Practice

from collections import defaultdict

words = ["apple", "ant", "banana", "ball", "cat", "car"]

groups = defaultdict(list)

for word in words:
    groups[word[0]].append(word)

print(dict(groups))