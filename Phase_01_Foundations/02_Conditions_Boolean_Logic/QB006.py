# Q6. Write a Python program that returns true if the two given integer values are equal or their sum or
# difference is 5

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))

print(True if a==b or (a+b==5) or abs(a-b==5) else False)

# Important point here is i am using abs() to eliminate negative value.
