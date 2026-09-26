# Q21. Write a Python program to get the size of an object in bytes.

import sys
name = 'Bhushan'

print(sys.getsizeof(name)) # Returns size in bytes

# List of integers

lst = [1,2,3,4,5]
print(sys.getsizeof(lst)) # Only measures the list pointer structure, not the integers

# Alternate Solution

import sys

text = input("Enter text: ")

print("Size:", sys.getsizeof(text), "bytes")