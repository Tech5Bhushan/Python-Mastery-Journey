# Q16. Write a Python program to print without a newline or space.

# Solution 1: Without Newline

print("Hello",end="")
print("World")

# Solution 2: Print Multiple Values Without Spaces

print("Python", end="")
print("3.13", end="")
print("Tutorial")

# Solution 3: Using sep=""

print("Hi","Bhushan",",""How" "are" "you?",sep="")


# Q2. What is the difference between sep and end?
# print("A", "B", "C", sep="-")
# Output = A-B-C
# sep controls the separator between values.
#
# print("A", end="")
# end controls what is printed after the values.