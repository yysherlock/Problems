import heapq

graph = {} # map of map
V = set()
with open('edges.txt') as f:
    N,M = map(int, f.readline().strip().split())
    for line in f:
        v1,v2,cost = map(int,line.strip().split())
        V.add(v1)
        V.add(v2)
        graph.setdefault(v1,{})
        graph.setdefault(v2,{})
        graph[v1][v2] = cost
        graph[v2][v1] = cost

loss = 0
X = set({1}) # source vertex: 1
v = 1
h = []
for i in range(N-1):
    #print(X)
    #X.add(v)
    #V.remove(v)
    for u,cost in graph[v].items():
        if u not in X:
            #print(True)
            heapq.heappush( h, (cost, v, u) )

    while True:
        c,v,u = heapq.heappop(h)
        if u not in X: break
    print('c:',c)
    loss += c
    #v = u
    X.add(u)
    V.remove(u)
    v = u
    print(X)

print(loss)
