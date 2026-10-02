# Q45. Write a Python program to compute and print the sum of two given integers (greater or equal to
# zero). In the event that the given integers or the sum exceed 80 digits, print overflow. Input first
# integer 25 Input second integer 22 Sum of the two integers 47

a = int(input("Enter the 1st integer: "))
b = int(input("Enter the 2nd integer: "))

if a < 0 or b < 0:
    print("Only non-negative integers are allowed")
else:
    total = a + b

    if len(str(a)) > 80 or len(str(b)) > 80 or len(str(total)) > 80:
        print("overflow")
    else:
        print("Sum:", total)