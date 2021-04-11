# 2) (Concept: Calling a function that has already been defined.)
# Below we are defining a function to sum two numbers. Right below that, we are calling this function two times, 
# but we have made a mistake while calling the function the first time. What's the mistake? Fix it.

def sum_two(a,b):
	answer = a + b
	return answer
	
result3 = sum_two(3, 4)
print(result3)
result4 = sum_two(5,6)
print(result4)

