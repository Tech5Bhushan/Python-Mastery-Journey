# Q8. Write a Python program to find the total number of even or odd divisors of a given integer.

num = int(input("Enter the Number: "))

ev_count=0
odd_count = 0
for i in range(1,num+1):
    if num % i == 0:
        if i % 2 == 0:
            ev_count = ev_count + 1
        else:
            odd_count = odd_count + 1

print("The count of even divisors is :",ev_count)
print("The count of odd divisors is :",odd_count)


# More Pythonic Version

num = int(input("Enter the Number: "))

even_divisors = sum(1 for i in range(1, num + 1)
                    if num % i == 0 and i % 2 == 0)

odd_divisors = sum(1 for i in range(1, num + 1)
                   if num % i == 0 and i % 2 != 0)

print("Even divisors:", even_divisors)
print("Odd divisors:", odd_divisors)