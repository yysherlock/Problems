"""
def setElem(index,elem,l):
    if index==len(l):
        l.append(elem)
    elif index < len(l):
	l[index] = elem
    else:
	print 'setElem: error parameter, index > len(l)'
	pass
"""

def generateSubset(S,subset,pos,selectpos):
    
    print subset
    for i in range(selectpos,len(S)):# select elem from S[selectpos:len(S)]
	    			     # to feed subset ith pos
	cur = S[i]
	selectpos = i + 1
#	setElem(pos,cur,subset) # increase elem step at ith pos
	subset.append(cur)
	generateSubset(S, subset,pos + 1,selectpos)
	# recover, prepare for change another elem at ith pos
	subset.pop(-1)

generateSubset([1,2,3,4],[],0,0)

