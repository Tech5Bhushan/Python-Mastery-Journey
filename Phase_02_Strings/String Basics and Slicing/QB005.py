# Q5. Write a Python program to remove words from a given list of strings containing a character or
# string.

words = ["apple", "banana", "orange", "grapes"]

ip = input("Enter the character or string name to remove from list: ")

e_lst = []

for word in words:
    if ip not in word:
        e_lst.append(word)

print(e_lst)

# Most Pythonic Version

words = ["apple", "banana", "orange", "grapes"]

ip = input("Enter the character or string name to remove from list: ")

result = [word for word in words if ip not in word]

print(result)