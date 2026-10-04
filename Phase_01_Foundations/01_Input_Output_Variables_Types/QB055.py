# Q55. Write a Python program that takes a positive integer and creates an N x N square filled with the
# integer N. Display the N x N square.

ip = int(input("Enter the N value: "))

matrix = []

for i in range(ip):
    row = []
    for j in range(ip):
        row.append(ip)

    matrix.append(row)

print(matrix)

# Most Pythonic Solution

n = int(input("Enter the N: "))

matrix = [[n] * n for _ in range(n)]

for row in matrix:
    print(row)
