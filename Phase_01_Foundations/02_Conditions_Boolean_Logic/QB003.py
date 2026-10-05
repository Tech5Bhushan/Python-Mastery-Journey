# Q3. Write a Python program that determines whether a given number (accepted from the user) is even
# or odd, and prints an appropriate message to the user.

num = int(input("Enter the number: "))

if num % 2 == 0:
    print("Hello user the number is EVEN")
else:
    print("Hello user the number is ODD")