# Q57. Write a Python program to find numbers that are greater than 10 and have odd first and last
# digits.

num = input("Enter the number :")
if int(num) > 10 and int(num[0]) % 2 != 0 and int(num[-1]) % 2 !=0:
    print("The num is greater than 10 and have odd 1st and last digit")
else:
    print("The num is either less than 10 or dont have 1st or last digit Odd")

