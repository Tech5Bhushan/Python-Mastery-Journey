# Q16. Write a Python program to get the ASCII value of a character.

ch = input("Enter the character: ")
print(ord(ch))

# Safer Version

ch = input("Enter a character: ")

if len(ch) == 1:
    print("ASCII value:", ord(ch))
else:
    print("Please enter only one character.")

# Reverse Operation --> EXTRA

# To convert an ASCII value back to a character, use chr():
# print(chr(65))