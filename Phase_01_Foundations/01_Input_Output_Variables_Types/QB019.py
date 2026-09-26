# Q19. Write a Python program to convert all units of time into seconds

days = int(input("Enter the number of Days: "))
hours = int(input("Enter the hours: "))
min = int(input("Enter the Min: "))
sec = int(input("Enter the sec: "))

print("Days in seconds = ",days*24*60*60,"\nHours in seconds = ",hours*60*60,"\nMin in seconds: ",min*60,"\nseconds = ",sec)

total = (days*24*60*60)+(hours*60*60)+(min*60)+sec
print("Total seconds:",total)
