# Q32. Write a Python program to calculate the time runs (difference between start and current time) of a
# program.

import time

start_time = time.time()

# Program code
for i in range(1000000):
    pass

end_time = time.time()

print("Execution time:", end_time - start_time, "seconds")

# Explanation
# time.time() - Returns the current time in seconds since January 1, 1970 (Unix Epoch).

# ALTERNATE METHOD

# More Accurate Method (perf_counter) - perf_counter() is recommended for measuring program performance because it provides higher precision.

import time

start_time = time.perf_counter()

for i in range(10000):
    pass

end_time = time.perf_counter()

print("The execution time is: ", end_time - start_time,"seconds")