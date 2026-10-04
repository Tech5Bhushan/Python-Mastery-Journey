# Q53. Write a Python program to check whether a given month and year contains a Monday 13th. Month
# No. 11 Year 2022 Check whether the said month and year contains a Monday 13th. False Month No. 6
# Year 2022 Check whether the said month and year contains a Monday 13th. True

from datetime import date

month = int(input("Enter the Month Number: "))
year = int(input("Enter the Year Number: "))

day_13 = date(year,month,13)

if day_13.weekday()==0:
    print(True)
else:
    print(False)


# Best Practice

from datetime import date

month = int(input("Month: "))
year = int(input("Year: "))

print(date(year, month, 13).weekday() == 0)

# Interview Question
#
# What does weekday() return for Friday?
#
# date(2022, 7, 1).weekday()
# OutPut : 4
#
# Reason :
# Monday = 0
# Tuesday = 1
# Wednesday = 2
# Thursday = 3
# Friday = 4
# Saturday = 5
# Sunday = 6