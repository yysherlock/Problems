def generatePermutation(prefix, S):
#    print('generatePermutation - ', 'prefix: ', prefix, 'S: ', S)
    if len(S)==0:
        print(prefix)
        return
    else:
        for i in range(len(S)):
#            print('i: ', i, 'prefix: ', prefix, 'S: ', S)
            cur = S[i]
            S.pop(i)
            generatePermutation(prefix+[cur], S)
            S.insert(i, cur)

def perm(n):
    S = [i for i in range(1,n+1)]
    return generatePermutation([], S)

#perm(3)
perm(4)
