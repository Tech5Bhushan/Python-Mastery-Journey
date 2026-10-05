# Q12. Write a Python program to check whether a given string contains a capital letter, a lower case
# letter, a number and a minimum length.

text = input("Enter a string: ")

if (len(text) >= 8 and
        any(ch.isupper() for ch in text) and
        any(ch.islower() for ch in text) and
        any(ch.isdigit() for ch in text)):

    print("Valid String")
else:
    print("Invalid String")


# Alternative Beginner-Friendly Solution

text = input("Enter a string: ")

upper = False
lower = False
digit = False

for ch in text:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True

if len(text) >= 8 and upper and lower and digit:
    print("Valid String")
else:
    print("Invalid String")