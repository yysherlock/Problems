
a,b,c = 6,3,1
x = 4

step = 0
visited_states = set({})

def search(S,sol):
    global step
    global visited_states
    global x
    print sol
    visited_states.add(tuple(sol))

    if x in sol: 
	return 1 # find target
    #step += 1
    for i in range(len(S)):
	for j in range(i+1,len(S)):
	    # pour water from ith cup to jth cup
	    if sol[i]>0 and sol[j]<S[j]:
		transfer = min(S[j]-sol[j],sol[i])
		sol[i] -= transfer
		sol[j] += transfer
#		print 'sol1:',sol
#		print 'visited:',visited_states
		if tuple(sol) in visited_states:
#		    print 'seen state:',sol
		    sol[i] += transfer
		    sol[j] -= transfer
		    continue
		if search(S,sol): return 1
		sol[i] += transfer
		sol[j] -= transfer
	    # pour water from jth cup to ith cup
	    if sol[j]>0 and sol[i]<S[i]:
		transfer = min(S[i]-sol[i],sol[j])
		sol[j] -= transfer
		sol[i] += transfer
#		print 'sol2:',sol
		if tuple(sol) in visited_states:
		    sol[j] += transfer
		    sol[i] -= transfer
		    continue
		if search(S,sol): return 1
		sol[j] += transfer
		sol[i] -= transfer
    return 0

search([a,b,c],[6,0,0])
