# Q4. Write a Python program to check if a substring presents in a given list of string values.

words = ["apple", "banana", "orange", "grapes"]

substring = input("Enter the substring: ")

found = False

for word in words:
    if substring in word:
        found = True
        break

print(found)

# Simpler Pythonic Solution

words = ["apple", "banana", "orange", "grapes"]

substring = input("Enter the substring: ")

print(any(substring in word for word in words))

