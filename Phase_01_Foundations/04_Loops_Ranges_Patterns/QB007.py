# Q7. Write a Python program to create a string consisting of non-negative integers up to n inclusive.

n = int(input("Enter the number: "))

for num in range(0, n + 1):
    print(num, end="")

# Alternate:

n = int(input("Enter the number: "))

print("".join(str(i) for i in range(n + 1)))

#Alternate

n = int(input("Enter n: "))

result = ""

for i in range(n + 1):
    result += str(i)

print(result)