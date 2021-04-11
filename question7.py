# Write a function named sum_to that accepts a single integer, n, and returns the sum of the 
# integers from 1 to n.

# For example:

# sum_to(6)  # returns 21
# sum_to(10) # returns 55
# (Hint 1: if you're having trouble, try to do it without a function first.)
# (Hint 2: You will need to define a function of the form def sum_to(...) and then you can call the function with 
# various inputs for the arguments such as 6 and 10, as shown in the examples above.
# (Hint 3: Your function definition will require parameters to act as a placeholder for the incoming input. 
# How many parameters will you need?)
# (Hint 4: In your function definition, you will need a for in range loop going from 1 to some number n that your 
# function should receive as an incoming parameter.)
# (Hint 5: If your code isn't working, try the python visualizer. )


def sum_to(n):
    total_sum = 0
    for x in range(n+1):
        total_sum += x
        print(total_sum)
    return total_sum
        
    

result = sum_to(6)
print(result)