
def generateSubset(S,bitmap,pos):
    if pos == len(S):
	print [S[i] for i in range(len(bitmap)) if bitmap[i]]
	return

    bitmap[pos] = 1
    generateSubset(S,bitmap,pos+1)
    bitmap[pos] = 0
    generateSubset(S,bitmap,pos+1)

S = [1,2,3,4]
bitmap = [0 for i in range(len(S))]
generateSubset(S,bitmap,0)
