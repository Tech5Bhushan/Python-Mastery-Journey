# Q17. Write a Python program to find the largest and smallest digits of a given number.

num = input("Enter the Number: ")
largest = int(num[0])
smallest = int(num[0])

for digit in num:
    if int(digit)>largest:
        largest = int(digit)
    elif int(digit)<smallest:
        smallest = int(digit)
print("The largest number is:",largest,"and","The smallest number is:",smallest)

# Slight Improvement

# Convert the digit only once inside the loop:

num = input("Enter the Number: ")

largest = int(num[0])
smallest = int(num[0])

for digit in num:
    digit = int(digit)

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

print("Largest digit:", largest)
print("Smallest digit:", smallest)


# Alternate Pythonic Solution

num = input("Enter the Number: ")

digits = [int(digit) for digit in num]

print("Largest digit:", max(digits))
print("Smallest digit:", min(digits))
