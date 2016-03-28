
def print_subset(num,S):
    """ num is a binary representation of bitmap """
    subset = []
    # using bitwise map num to construct subset
    for i in range(len(S)):
	# 1<<i is 0..010..0, ith pos from rightmost is 1, others are zeros
	if num & (1<<i): # check whether or not ith element of S is in subset 
	    subset.append(S[i])
    print subset

# print_subset(3,['a','b','c']) #['a','b']

def generateSubset(S):
#   for i in range(2**len(S)):
    for i in range(1<<len(S)):
	print_subset(i,S)

generateSubset([1,2,3,4])
