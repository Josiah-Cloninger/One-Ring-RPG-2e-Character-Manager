# Python3 code to demonstrate
# Append K character N times
# using ljust()

# initializing string 
test_string = 'GFG'

# printing original string 
print("The original string : " + str(test_string))

# initializing K 
K = 'M'

# No. of K required
N = 5

# using ljust()
# Append K character N times
res = test_string.ljust(N + len(test_string), K)

# print result
print("The string after adding trailing K : " + str(res))
