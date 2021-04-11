# 3)(Concept: Defining a function)
# Below we are defining a function to multiply two numbers. After that, we are calling this function two 
# times, 
# and storing the results in variables. But this is failing due to a mistake while defining the function. 
# What's the mistake? Fix it.

def multiply(num1,num2):
    answer = num1 * num2
    return answer

result5 = multiply(10,10)
print(result5)

result6 = multiply(5,6)
print(result6)