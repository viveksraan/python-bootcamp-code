def list_n_1(n):
    return [str(num) for num in range(n)]

def list_n_2(n):
    return list(map(str, range(n)))

import time

# Analizing time taken for the first functionality
# Current time before the execution started
start_time1 = time.time()
# Running the code
list1 = list_n_1(1000000)
# Current time after the code is fully executed
end_time1  = time.time()
# Elapsed time
time_taken1 = end_time1 - start_time1

# Analizing time taken for the first functionality
# Current time before the execution started
start_time2 = time.time()
# Running the code
list2 = list_n_2(1000000)
# Current time after the code is fully executed
end_time2  = time.time()
# Elapsed time
time_taken2 = end_time2 - start_time2

# Comparing both the timings you will see that the second functionality is bit faster but if you will test the same functions on a smaller arguments such as 1 you might end up getting 0 elapsed time for both the functions so precision of time module is lesser because of which timeit module is generaly more preferred
print("First time is " + str(time_taken1))
print("Second time is " + str(time_taken2))
