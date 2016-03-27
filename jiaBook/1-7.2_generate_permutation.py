
def generatePermutation(prefix,S):
    if len(S) == 0: print prefix
    else:
        for i in range(len(S)):
	    if i>0 and S[i]==S[i-1]: continue # add this line to deal with the duplicate elements
            cur = S[i]
            S.pop(i)
	    generatePermutation(prefix+[cur], S)
	    S.insert(i,cur)

def perm(S=[],n=1):
    if not S: S = [i+1 for i in range(n)]
    generatePermutation([],S)

perm(n=3)
perm(n=4)
perm(S=[1,1,2])
