# Q10. Write a Python program that accepts an integer and determines whether it is greater than 4^4
# and which is 4 mod 34.

num = int(input("Enter the number: "))

print(True if (num> 4**4) and (num%34) == 4 else False)