# Q12. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given
# string. Return n copies of the whole string if the length is less than 2.

text = input("Enter the string: ")
n = int(input("Enter number of copies: "))

if len(text)<2:
    print(text * n)
else:
    print(text[:2]*2)
