# Q4. Write a Python program to test whether a passed letter is a vowel or not.

a = input("Enter the LETTER: ")
lst = ['a','e','i','o','u','A','E','I','O','U']

if a in lst:
    print("The letter is VOWEL")
else:
    print("The letter is NOT vowel")

# Better Version

a = input("Enter the LETTER: ").lower()
lst = ['a','e','i','o','u']

if a in lst:
    print("The letter is VOWEL")
else:
    print("The letter is NOT vowel")

# Most Pythonic Version

letter = input("Enter the LETTER: ").lower()

if letter in "aeiou":
    print("The letter is VOWEL")
else:
    print("The letter is NOT vowel")

# Small Improvement
# To ensure the user enters only one letter:

letter = input("Enter a letter: ").lower()

if len(letter) == 1 and letter in "aeiou":
    print("The letter is VOWEL")
else:
    print("The letter is NOT vowel")

