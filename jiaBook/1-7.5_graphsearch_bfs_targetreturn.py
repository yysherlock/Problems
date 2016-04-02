from collections import deque
from copy import deepcopy
import sys

start = [[2,6,4],[1,3,7],[0,5,8],[2,0],0]
target = [[8,1,5],[7,3,6],[4,0,2],[2,1],-1]

def search():
    #global start, emptyx, emptyy
    #emptyx,emptyy = 2,0 # empty slot position: (emptyx, emptyy)

    dist = [0]
    found = 0
    cnt = 0
    q = deque([start])
    visited = set({})
    visited.add(str(start[:-1]))

    while len(q)>0:
        cur = q.popleft()
        #print cur
        ##if step == 10: sys.exit(1)
        ##step += 1
        if cur[:-1] == target[:-1]:
            found = 1 # find target
            break
        else:
            emptyx,emptyy = cur[-2]
            parentIdx = cur[-1]

            for shift in [[-1,0],[1,0],[0,-1],[0,1]]: # empty slot shift to up, down, left, right
                shiftedx, shiftedy = emptyx+shift[0],emptyy+shift[1]
                if shiftedx>=0 and shiftedx<3 and shiftedy>=0 and shiftedy<3:
                    # (shiftedx,shiftedy) is valid, get a valid neighbor of cur
                    neighbor = deepcopy(cur)
                    neighbor[emptyx][emptyy],neighbor[shiftedx][shiftedy] = neighbor[shiftedx][shiftedy], neighbor[emptyx][emptyy]
                    neighbor[-2] = [shiftedx,shiftedy]

		    if str(neighbor[:-1]) not in visited:
                        cnt += 1
                        neighbor[-1] = cnt
                        dist.append(dist[parentIdx] + 1)
			visited.add(str(neighbor[:-1]))
                        q.append(neighbor)

    if found:
        print dist[cur[-1]]
    else:
        print -1


search()
