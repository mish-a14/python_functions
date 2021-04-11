# # 6) 
# (Concept: Defining a function).
# First, Define a function called greater_than_5 that accepts one parameter will return True if the incoming
# input is greater than 5, and returns False if the incoming is less than or equal to 5. Secondly, call this
#  function at least two times and print out the result both times.

def greater_than_five(a): 
    if a > 5:
        return True
    elif a <= 5:
        return False 


result = greater_than_five(6)
print(result)

result1 = greater_than_five(2)
print(result1)