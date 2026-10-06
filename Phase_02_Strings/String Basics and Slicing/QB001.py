# Q1. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# 		Sample List : ['abc', 'xyz', 'aba', '1221']
# 		Expected Result : 2

lst = ['abc', 'xyz', 'aba', '1221']
e_lst = []
for item in lst:
    if len(item) >= 2 and item[0] == item[-1]:
        e_lst.append(item)
print(e_lst)

