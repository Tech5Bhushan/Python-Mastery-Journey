# Q1. Write a Python program to compute the sum of digits of each number of a given list.

lst = [12,23,34,45,56]
e_lst = []

for num in lst:
    total = 0
    for digit in str(num):
        total = total + int(digit)
    e_lst.append(total)
print(e_lst)



