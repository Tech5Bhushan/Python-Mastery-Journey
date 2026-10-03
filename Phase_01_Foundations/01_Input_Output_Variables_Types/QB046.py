# Q46. Write a Python program that reads a date (from 201611 to 20161231) and prints the day of the
# date. Jan. 1, 2016, is Friday. Note that 2016 is a leap year.


from datetime import date, datetime

date_input = input("Enter the date in YYYYMMDD Format: ")

try:
    entered_date = datetime.strptime(date_input, "%Y%m%d")

    if entered_date.year == 2016:
        print("Day: ",entered_date.strftime("%A"))
    else:
        print("Error: Enter a date from the year 2016.")

except ValueError:
    print("Error: Enter a valid date in YYYYMMDD format.")


# SOME BASICS ABOUT DATE TIME.
