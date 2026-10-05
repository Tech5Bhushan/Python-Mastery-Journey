# Q8. Write a Python program that converts seconds into days, hours, minutes, and seconds.

# Formula :
# 1 Day = 24 Hrs = 24 * 3600 secs = 86400 secs
# 1 Hr = 60 Mins = 3600 secs
# 1 Min = 60 Secs

seconds = int(input("Enter the seconds: "))

days = seconds // 86400
seconds %= 86400

hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

print("Days    :", days)
print("Hours   :", hours)
print("Minutes :", minutes)
print("Seconds :", seconds)


# Using divmod() (Pythonic Version)


seconds = int(input("Enter the seconds: "))

days, rem = divmod(seconds, 86400)
hours, rem = divmod(rem, 3600)
minutes, seconds = divmod