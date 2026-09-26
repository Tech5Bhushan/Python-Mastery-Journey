# Q9. Write a Python program that checks whether a specified value is contained within a group of values.

# This question is usually solved using the in operator.

# SOLUTION 1 :

values = [1, 5, 8, 3]

num = int(input("Enter a number: "))

if num in values:
    print(True)
else:
    print(False)

# SOLUTION 2:

values = [1, 5, 8, 3]

num = int(input("Enter a number: "))
print(num in values)

# SOLUTION 2: Using Tuple

data = (1, 5, 8, 3)

print(3 in data)
print(-1 in data)

