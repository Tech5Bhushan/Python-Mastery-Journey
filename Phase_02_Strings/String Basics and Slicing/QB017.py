# Q17. Write a Python program to define a string containing special characters in various forms.

import string

text = "Hell& Bhu$han #ow a^e y%u"
lst = []
for ch in text:
    if ch in string.punctuation:
        lst.append(ch)

print("special characters",lst)

# More Pythonic Version

import string

text = "Hell& Bhu$han #ow a^e y%u"

special_chars = [ch for ch in text if ch in string.punctuation]

print(special_chars)