
import math

case = 0
t = int(raw_input())
while case < t:
    n,p,w,h = (int(x) for x in raw_input().split())
    a = [int(x) for x in raw_input().split()]
    result = w

    for i in range(w): # i:0~w-1, s: w~1
        s = w - i
        maxlines = p * (h/s)
        #print 's:',s,'maxlines:',maxlines
        curlines = 0
        found = 1
        for j in range(len(a)): # jth para.
            curlines += int(math.ceil(float(a[j])/(w/s)))
            if maxlines==0 or curlines > maxlines:
                found = 0
                break
            #print 'w:',w,'s:',s,"w/s:",w/s,'a[j]:',a[j]
            #print 'math.ceil(float(a[j])/(w/s)):',math.ceil(float(a[j])/(w/s))

        if found:
            print s
            break

    case += 1
