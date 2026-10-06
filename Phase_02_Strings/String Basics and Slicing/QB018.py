# Q18. Write a Python program to check whether a string is numeric.

text = input("Enter the numeric value: ")

print(text.isdecimal())  # Output: True
print(text.isdigit())    # Output: True
print(text.isnumeric())  # Output: True

# Difference Between isdigit() and isnumeric()

# text.isdigit() --> Checks for digit characters.

# text.isnumeric() --> Checks for numeric characters and is slightly more general.
