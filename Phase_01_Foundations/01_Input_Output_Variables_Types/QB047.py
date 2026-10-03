# Q47. Write a Python program to sum all numerical values (positive integers) embedded in a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()

print(words)

total = 0

for word in words:
    if word.isdigit():
        total += int(word)

print("Sum =", total)

# Solution Using Regular Expressions

import re

sentence1 = input("Enter the sentence: ")

numbers = re.findall(r'\d+',sentence)

total1 = sum(map(int,numbers))

print("Sum :",total1)

# Explaination - re.findall(r'\d+', sentence) --> It extracts all numbers from the sentence

