# Q13. Write a Python program to hash a word.

word = 'Bhushan'
hash_word = hash(word)

print(hash_word)

# Python provides the built-in hash() function to generate a hash value for a string.
# The exact hash value may be different on each run and system.
# Important Note
#
# The built-in hash() function is not suitable for cryptographic purposes, because Python may generate different hash values across different runs.
#
# If you need a consistent hash, use hashlib.
#
# Using MD5
#
# import hashlib
#
# word = input("Enter a word: ")
#
# hashed = hashlib.md5(word.encode())
#
# print(hashed.hexdigest())
