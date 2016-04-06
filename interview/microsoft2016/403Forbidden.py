
rules = []
# N rules, M requests
N,M = (int(x) for x in raw_input().split())

def ip2binstr(rip):
    ip = rip
    mask = 0
    result = ''
    if '/' in rip:
        ip,mask = rip.split('/')
        mask = int(mask)

    if mask > 0:
        for x in ip.split('.'):
            bp = bin(int(x))[2:]
            zeros = '0'*(8-len(bp))
            result = result + zeros + bp

    return (ip,mask,result[:mask])

def ip2binrep(ip,mask):
    result = ''
    for x in ip.split('.'):
        if len(result)>=mask: break
        bp = bin(int(x))[2:]
        zeros = '0'*(8-len(bp))
        result = result + zeros + bp
    return result[:mask]

for i in range(N):
    state,rip = raw_input().split()
    if state=='allow': state = 'YES'
    #elif state=='deny': state = 'NO'
    else: state='NO'
    ip,mask,binrep = ip2binstr(rip)
    rules.append([state,ip,mask,binrep[:mask]])

#print 'rules:',rules

for i in range(M):
    qip = raw_input()
    found = 0
    for rule in rules:
        state,ip,mask,prefix = rule
        if qip == ip:
            found = 1
            print state
            break
        else:
            if mask > 0:
                qbinrep = ip2binrep(qip,mask)
                #print 'qbinrep:',qbinrep
                if qbinrep == prefix:
                    found = 1
                    print state
                    break
    if not found:
        print 'YES'
