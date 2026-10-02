# Q40. Write a Python program that accepts a positive number and subtracts from it the sum of its digits,
# and so on. Continue this operation until the number is positive.

num = int(input("Enter the Positive number: "))
while(num>0):
    digit_sum = sum (int(digit) for digit in str(num))
    num = num - digit_sum
    print(num)


# Alternate Solution :

num = int(input("Enter a positive number: "))

while num:
    num -= sum(map(int, str(num)))
    print(num)