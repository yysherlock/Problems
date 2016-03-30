
def search(S,sol):
    global cnt

    #"""    
    if sol: print ''.join(sol)
    if cnt == N: return 0
    else: cnt += 1
    """
    if cnt == N:
	print ''.join(sol)
	return 0
    else: cnt += 1
    """

    for i in range(len(S)):
	cur = S[i]
	sol.append(cur)
        ok = 1
	for j in range(len(sol)):
	    if 2*j>=len(sol) and sol[j:] == sol[j-(len(sol)-j):j]: 
	        ok = 0
		break
	if ok:
	    if not search(S,sol): return 0
	sol.pop(-1)
        
    return 1

#S = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',\
#	'P','Q','R','S','T','U','V','W','X','Y','Z']

L = 3 # use first L characters
N = 7 # find Nth hard string
cnt = 0

search(['A','B','C'],[])

