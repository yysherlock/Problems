from collections import deque

def generatePermutation(prefix,S):
    if len(S) == 0: print prefix
    else:
        for i in range(len(S)):
            cur = S[i]
	    if cur not in prefix:	
		S.pop(i)
	        generatePermutation(prefix+[cur], S)
		S.insert(i,cur)

def perm(n):
    S = [i+1 for i in range(n)]
    generatePermutation([],S)

perm(3)
perm(4)
