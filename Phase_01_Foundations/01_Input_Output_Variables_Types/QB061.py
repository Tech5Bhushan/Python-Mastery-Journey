# Q61. Write a Python program to find an integer (n >= 0) with the given number of even and odd digits.

even_count = int(input("Enter number of even digits: "))
odd_count = int(input("Enter number of odd digits: "))

number = "2" * even_count + "1" * odd_count

print("Required number:", number)

# If the question means "count even and odd digits in a given number"

num = input("Enter a number: ")

even = 0
odd = 0

for digit in num:
    if int(digit) % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even digits:", even)
print("Odd digits:", odd)