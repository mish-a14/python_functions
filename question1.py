# 1) (Concept: Calling a function that has already been defined.)

# The following function definition defines a function called pokemon_contains that will tell you if a single 
# incoming_letter passed into this function exists in the word "pokemon". This function returns a boolean 
# (ie., True or False). Your task is to first, copy this function and then call this function by passing in the 
# letter "k". 
# Store the result of this function call in a variable called result1. 
# Print out the result. 
# Secondly, call this function by passing in the letter "o". Store the result of this function call in a variable 
# called result1. 
# Print out the result.

def pokemon_contains(incoming_letter):
	if incoming_letter in "pokemon":
		return True
	else:
		return False

result = pokemon_contains('k')
print(result)

result1 = pokemon_contains('o')
print(result1)