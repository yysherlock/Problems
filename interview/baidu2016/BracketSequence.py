
result = {}
#global cost
cost = []

def check(s):
    left, right = 0, 0
    for c in s:
        if left < right: return False
        if c == '(': left += 1
        if c == ')': right += 1
    if left == right:
        return True
    else: return False

def generate(seq, pos, val, costIdx):
    #global result

    #print pos, ''.join(seq)
    if pos == len(seq):
        seq = ''.join(seq)
        if check(seq):
            print 'valid:',seq
            if '?' not in seq and val not in result.keys(): result[val] = seq

    for i in range(pos,len(seq)):
        if not seq[i] == '?':
            generate(seq, i+1, val, costIdx)
        else :
            seq[i] = '('
            generate(seq, i+1, val + cost[costIdx][0], costIdx+1)
            seq[i] = ')'
            generate(seq, i+1, val + cost[costIdx][1], costIdx+1)
            seq[i] = '?'

while True:
    #global cost
    seq = raw_input()
    m = 0
    for c in seq:
        if c == '?': m+=1

    for i in range(m):
        cost.append( [int(x) for x in raw_input().split()] )

    # enum
    generate(list(seq),0,0,0)
    print 'result:',result
    print min(result)
    result = {}
    cost = []

    """
    m = 0
    for c in seq:
        if c == '?': m+=1
    for i in range(m):
        lcost, rcost = [int(x) for x in raw_input().split()]

    """
"""
(??)
1 2
2 8
"""
