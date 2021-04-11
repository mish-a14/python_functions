# Write a function named largest that takes a list of numbers as 
# an argument and returns the largest number in that 
# list.

# For example:

# largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 231


def largest(numbers):
    largest_number_so_far = 0
    for n in numbers:
        if n >= largest_number_so_far:
            largest_number_so_far = n
            print(n)
            #largest_number_so_far
    return largest_number_so_far

result = largest([1,2,4,5,3,5,2,200,100])
print(result)
