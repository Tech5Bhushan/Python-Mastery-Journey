# Q4. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)

# SOLUTION 1 :

exam_st_date = (11, 12, 2014)
print("The examination will start from : %i/%i/%i" % exam_st_date)

#SOLUTION 2: Using f-string

exam_st_date = (11, 12, 2014)
print(f"The examination will start from : {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}")

# SOLUTION 3: Using Indexing

exam_st_date = (11, 12, 2014)
print("The examination will start from :",exam_st_date[0],"/",exam_st_date[1],"/",exam_st_date[2])