# 4) 
# (Concept: Functions are not executed until called.)
# If we run the program below, in what order will the 3 print statements be executed? 
# Before you submit your answer, verify your theory by running your code, and also by trying it in the python 
# visualizer.

def multiplication(a,b):
	my_answer = a*b
	print("Calculating...")
	return my_answer

print("Let's Multiply stuff...")
answer = multiplication(5,6)
answer = str(answer)
print("The answer is..." + answer)



# ANS: the print statements will run in the following order: 
# print('calculating...')
# print("Let's Multiply stuff...")
# print("The answer is..." + answer)

#this is wrong because I just checked the debugger. before the function is even performed- the print("Let's Multiply 
# stuff...") is printed first 
# then the print('calculating...') is printed. 

#I am not too entirely sure of this order but I will try to look into it. 