
rules = {}
maskrules = {} # mask:[[shared prefix1:state], [shared prefix2:state]]
# N rules, M requests
N,M = (int(x) for x in raw_input().split())

def ip2binstr(rip):
    ip = rip
    mask = 0
    result = ''
    if '/' in rip:
        ip,mask = rip.split('/')
        mask = int(mask)

    for x in ip.split('.'):
        bp = bin(int(x))[2:]
        zeros = '0'*(8-len(bp))
        result = result + zeros + bp

    if mask > 0:
        return (ip,mask,result[:mask])
    else: return (ip,mask,result)


for i in range(N):
    state,rip = raw_input().split()
    if state=='allow': state = 'YES'
    else: state = 'NO'
    ip,mask,binrep = ip2binstr(rip)
    if mask > 0:
        maskrules.setdefault(mask,{})
        maskrules[mask][binrep] = state
    else:
        rules[ip] = state

for i in range(M):
    ip = raw_input()
    found = 0
    if ip in rules.keys():
        found = 1
        print rules[ip]
    else:
        binrep = ip2binstr(ip)
        for k,v in maskrules.items():
            if binrep[:k] in v.keys():
                found = 1
                print v[binrep[:k]]
                break
    if not found:
        print 'YES'
