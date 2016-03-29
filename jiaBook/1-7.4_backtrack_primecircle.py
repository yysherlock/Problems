
n = 6

# generate prime table
def generatePrimeTable(num):
    """ Generate a prime table p[0,1,...,n-1],
    p[i]=1 indicates that i is a prime. """
    return [i for i in range(2,num+1) if is_prime(i)]

def is_prime(i):
    for j in range(2, i):
        if j * j > i: break
	if i % j == 0: return False
    return True
"""
print is_prime(2)
print is_prime(4)
print is_prime(13)
print is_prime(14)
print is_prime(53)
print is_prime(63)
"""
isp = generatePrimeTable(n)
vis = [0 for i in range(n)]
vis[0] = 1 # use vis array, you can save a NextSelectPos parameter for the recursive function

def search(S,sol,pos):
    if pos == n and is_prime(sol[0]+sol[-1]):
	print sol
        return
    for i in range(1,len(vis)):
	curselect = S[i]
	if not vis[i] and is_prime(sol[-1]+curselect):
	    sol.append(curselect)
	    vis[i] = 1
            search(S,sol,pos+1)
	    sol.pop(-1)
	    vis[i] = 0
    
search([1,2,3,4,5,6],[1],1)

