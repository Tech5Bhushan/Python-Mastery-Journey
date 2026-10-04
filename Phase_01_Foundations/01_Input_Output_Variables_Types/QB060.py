# Q60. Write a Python program to find all 5's in integers less than n that are divisible by 9 or 15.

n = int(input("Enter the number: "))

count = 0

for i in range(n):
    if i % 9 == 0 or i % 15 ==0:
        count = count + str(i).count('5')

print("The count of number of 5's: ",count)