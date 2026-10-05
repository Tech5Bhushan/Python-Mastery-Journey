# Q2. Write a Python program to get the weighted average of two or more numbers.

values = [1,2,3]
weighted = [5,6,7]

weighted_sum = 0

for i in range(len(values)):
    weighted_sum = weighted_sum + (values[i]*weighted[i])

weighted_avg = weighted_sum / sum(weighted)

print("Weighted AverageL: ",weighted_avg)


# Pythonic Solution

values = [10, 20, 30]
weights = [1, 2, 3]

weighted_average = sum(v * w for v, w in zip(values, weights)) / sum(weights)

print(weighted_average)
