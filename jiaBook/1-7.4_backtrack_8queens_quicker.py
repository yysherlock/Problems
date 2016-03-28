
n = 8

def print_sol(sol):
    for i in range(len(sol)):
       print '('+str(i)+','+str(sol[i])+')',
    print ''
# vis list of list 3 x n
vis = []
for i in range(3):
    vis.append([])
    for j in range(2*n):
	vis[-1].append(0)

def search(sol,row):
    """ use a simple data structure to quickly check whether current solution
    is valid or not """
    if row == n:
	print_sol(sol)
	return
    for col in range(n):
	# vis[0][x]: x th column is occupied or not
	# vis[1][x]: x th diagonal is occupied or not
	# vis[2][x]: x th secondary diagonal is occupied or not
	if (not vis[0][col]) and (not vis[1][col-row+n]) and (not vis[2][col+row]):
	    sol.append(col)
	    vis[0][col] = vis[1][col-row+n] = vis[2][col+row] = 1
	    search(sol,row+1)
	    vis[0][col] = vis[1][col-row+n] = vis[2][col+row] = 0
	    sol.pop(-1)
	
    
search([],0)

