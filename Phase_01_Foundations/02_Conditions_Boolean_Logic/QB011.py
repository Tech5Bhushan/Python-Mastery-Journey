# 77. Write a Python program to convert GPAs to letter grades according to the following table:
# GPAs	Grades
# 4.0:	A+
# 3.7:	A
# 3.4:	A-
# 3.0:	B+
# 2.7:	B
# 2.4:	B-
# 2.0:	C+
# 1.7:	C
# 1.4:	C-
# below:	F
# Input:
# [4.0, 3.5, 3.8]
# Output:
# ['A+', 'A-', 'A']
# Input:
# [5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]
# Output:
# ['A+', 'A+', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'F']


lst = [5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]

e_lst = []

for i in lst:
    if i >= 4.0:
        e_lst.append('A+')
    elif i >= 3.7:
        e_lst.append('A')
    elif i >= 3.4:
        e_lst.append('A-')
    elif i >= 3.0:
        e_lst.append('B+')
    elif i >= 2.7:
        e_lst.append('B')
    elif i >= 2.4:
        e_lst.append('B-')
    elif i >= 2.0:
        e_lst.append('C+')
    elif i >= 1.7:
        e_lst.append('C')
    elif i >= 1.4:
        e_lst.append('C-')
    else:
        e_lst.append('F')

print(e_lst)
