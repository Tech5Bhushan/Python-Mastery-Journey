# Q48. Write a Python program to print a given N by M matrix of numbers line by line in forward
# backwards forward ... order. Input matrix [[1, 2, 3,4], [5, 6, 7, 8], [0, 6, 2, 8], [2, 3, 0, 2]]

matrix = [[1, 2, 3,4],
          [5, 6, 7, 8],
          [0, 6, 2, 8],
          [2, 3, 0, 2]]

for i in range(len(matrix)):
    if i % 2 == 0:
        print(*matrix[i])
    else:
        print(*matrix[i][::-1])

# Explanation
# Check row number -->    if i % 2 == 0
#
# Even row index(0, 2, 4, ...) → Print normally.
# Odd row index(1, 3, 5, ...) → Print in reverse order.
#
# [::-1] creates a reversed copy of the sequence.
#
# Using enumerate:
print("====================")

matrix1 = [[1, 2, 3,4],
          [5, 6, 7, 8],
          [0, 6, 2, 8],
          [2, 3, 0, 2]]

for i,row in enumerate(matrix1):
    print(*(row if i % 2 == 0 else row[::-1]))