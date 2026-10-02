# Q43. Write a Python program to compute the digit number of the sum of two given integers.

a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))

ad = a+b

print("Addition: ",ad)
print("Number of Digits: ", len(str(ad)))


#Why this question is important because "object of type 'int' has no len()", so we need to typecast the final sum in string.