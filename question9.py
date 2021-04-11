# Write a function named occurances that takes two string 
# arguments as input and counts the number of 
# occurances of the second string inside the first string.

# For example:

# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0


def occurances(str, str_a):
    str_occurances = 0 
    for i, s in enumerate(str):
        if str_a in s:
            str_occurances += 1
    return str_occurances


result = occurances('fleep fleep', 'ee')
print(result)


#count function that counts number of times a string appears in another string 
#declae a counter variable inside the function set to zero and everytime s 