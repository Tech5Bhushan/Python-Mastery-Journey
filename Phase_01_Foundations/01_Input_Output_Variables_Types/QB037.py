# Q37. Write a python program to convert decimal to hexadecimal. Sample decimal number: 30, 4

# Solution 1: Using hex()

num = int(input("Enter a decimal number: "))

hexadecimal = hex(num)

print("Hexadecimal:", hexadecimal)

# Solution 2: Without the 0x Prefix

num1 = int(input("Enter a decimal number: "))

hexadecimal1 = hex(num1)[2:]

print(hexadecimal1)

# Solution 3: Using format()

num2 = int(input("Enter the decimal numer: "))

dec = format(num2 , 'x')

print(dec)


# Explanation
# hex(num) converts a decimal number to hexadecimal and includes the prefix 0x.
# hex(num)[2:] removes the 0x prefix.
# format(num, 'x') converts directly to lowercase hexadecimal.
# format(num, 'X') converts to uppercase hexadecimal.