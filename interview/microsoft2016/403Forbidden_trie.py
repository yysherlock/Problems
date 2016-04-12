
class ipRuleNode(object):
    def __init__(self, isRule = False, priority = 0, content = '', state = 'YES'):
        self.priority = priority
        self.content = content
        self.isRule = isRule
        self.state = state
        self.children = dict({})

    def insertNode(self, c):
        if not self.children: self.children = dict({})
        self.children[c] = ipRuleNode(content=self.content + c)

def ip2binstr(rip):
    # for rules
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

def ip2binrep(ip):
    # for queries
    result = ''
    for x in ip.split('.'):
        bp = bin(int(x))[2:]
        zeros = '0'*(8-len(bp))
        result = result + zeros + bp
    return result

# N rules, M requests
N,M = (int(x) for x in raw_input().split())

# build trie to store rules
trie = ipRuleNode()

for i in range(N):
    state,rip = raw_input().split()
    if state=='allow': state = 'YES'
    else: state='NO'
    ip,mask,binrep = ip2binstr(rip)
    s = binrep[:mask] if mask > 0 else binrep
    cur = trie
    for c in s:
        if c not in cur.children.keys():
            cur.insertNode(c)
        cur = cur.children[c]
    cur.isRule = True
    cur.state = state
    cur.priority = i # smaller, better

#print 'rules:',rules

for i in range(M):
    qip = raw_input()
    found = 0
    qbinrep = ip2binrep(qip)
    cur = trie
    matched = ('YES',N)
    for c in qbinrep:
        if cur.isRule and cur.priority < matched[1]:
            matched = (cur.state, cur.priority)
        if c in cur.children.keys():
            cur = cur.children[c]

    print matched[0]
