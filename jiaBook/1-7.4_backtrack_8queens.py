
n = 8 # n=4, (1,3,0,2) (2,0,3,1)

def print_sol(sol):
    for i in range(len(sol)):
	print '('+str(i)+','+str(sol[i])+')',
    print ''

#print_sol([1,2,0])

def search(sol,row):
    # decide which column to fill at row 
    if row == n: 
	print_sol(sol)
	return 
    for col in range(n):
	sol.append(col)
	# check current sol valid or not
        ok = 1
	for i in range(len(sol)-1):
	    # (row,col) and (i,sol[i])
	    if col==sol[i] or row-col==i-sol[i] or row+col==i+sol[i]:
		ok = 0
		break
	if ok: search(sol,row+1)
	sol.pop(-1)

search([],0)


