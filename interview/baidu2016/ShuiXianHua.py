m,n = [ int(x) for x in raw_input().split()]

re = ''
for i in range(m,n+1):
    org = i
    cubeSum = 0
    while i>0:
        cubeSum += (i % 10)**3
        i /= 10
    if cubeSum == org:
        re = re + str(org) + ' '

if re: print re.strip()
else: print 'no'
