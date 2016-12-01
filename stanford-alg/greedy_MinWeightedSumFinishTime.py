import heapq

with open('jobs.txt') as f:
    N = int(f.readline().strip())
    h = []
    loss = 0
    for line in f:
        w,l = map(int,line.strip().split())
        heapq.heappush(h, (l-w,-w,l))
    c = 0
    for i in range(N):
        d,w,l = heapq.heappop(h)
        d = -d; w = -w;
        c += l
        loss += w*c
    print(loss)

with open('jobs.txt') as f:
    N = int(f.readline().strip())
    h = []
    loss = 0
    for line in f:
        w,l = map(int,line.strip().split())
        heapq.heappush(h, (-w/l,-w,l))
    c = 0
    for i in range(N):
        d,w,l = heapq.heappop(h)
        d = -d; w = -w;
        c += l
        loss += w*c
    print(loss)
