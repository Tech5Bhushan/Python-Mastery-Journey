# Q20. Write a Python program to prove that two string variables of the same value point to the same
# memory location.

str1 = "Bhushan"
str2 = "Bhushan"

print("ID of str1:", id(str1))
print("ID of str2:", id(str2))

if id(str1) == id(str2):
    print("Both variables point to the same memory location.")
else:
    print("Both variables point to different memory locations.")


# Best Practice

str1 = "Python"
str2 = "Python"

print("Same memory location:", str1 is str2)
print("ID of str1:", id(str1))
print("ID of str2:", id(str2))