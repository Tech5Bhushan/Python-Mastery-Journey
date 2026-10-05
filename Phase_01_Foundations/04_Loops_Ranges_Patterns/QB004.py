# Write a Python program to print letters from the English alphabet from a-z and A-Z.
# Sample Input
# (Alphabet from a-z)
# (nAlphabet from A-Z)
# Sample Output
# Alphabet from a-z
# a b c d e f g h i j k l m n o p q r s t u v w x y z
# Alphabet from A-Z
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

import string

print("Alphabet from a-z: ")
for letter in string.ascii_lowercase:
    print(letter,end=" ")

print("\nAlphabet from A-Z: ")
for LETTER in string.ascii_uppercase:
    print(LETTER,end=" ")

# Beginner-Friendly Solution (Without string Module)

print("\nAlphabet from a-z")

for i in range(ord('a'),ord('z') + 1):
    print(chr(i),end=" ")

print("\nAlphabet from A-Z")

for i in range(ord('A'),ord('Z') + 1):
    print(chr(i),end=" ")


# Best Practice

import string

print("\nAlphabet from a-z")
print(*string.ascii_lowercase)

print("\nAlphabet from A-Z")
print(*string.ascii_uppercase)