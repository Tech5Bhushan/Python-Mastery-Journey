# Q41. Write a Python program to find the digits that are missing from a given mobile number.

# SOLUTION 1 :

# mbl_num = input("Enter the 10 digit mobile number: ")
#
# all_digits = set('0123456789')
# present_digits = set(mbl_num)
#
# missing_digits = all_digits - present_digits
#
# print(sorted(missing_digits))


#SOLUTION 2:

mbl_num1 = input("Enter the mobile number: ")

all_digi = '0123456789'
e_lst = []
for i in all_digi:
    if i not in mbl_num1:
        e_lst.append(i)

print(e_lst)