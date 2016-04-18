import math
n,m = [ int(x) for x in raw_input().split()]

re = 0
for i in range(m):
    re += n
    n= math.sqrt(n)

print "{0:.2f}".format(re)
