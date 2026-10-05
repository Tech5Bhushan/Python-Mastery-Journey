# Q2. Write a Python program to calculate the sum of three given numbers. If the values are equal, return
# three times their sum.

a = int(input("Enter the 1st Number: "))
b = int(input("Enter the 2nd Number: "))
c = int(input("Enter the 3rd Number: "))

if a==b==c:
    print("EQUAL,the sum will be 3 times:",3*(a+b+c))
else:
    print("The nums are NOT equal, and their sum is",a+b+c)


#Interview Friendly:

def cal_sum(a,b,c):
    total = a+b+c
    return total*3 if a==b==c else total

a = int(input("Enter the 1st Number: "))
b = int(input("Enter the 2nd Number: "))
c = int(input("Enter the 3rd Number: "))

print(cal_sum(a,b,c))