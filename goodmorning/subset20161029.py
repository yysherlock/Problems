def generateSubset(S, prefix, pos):
    # dfs
    print(prefix)
    for i in range(pos,len(S)): # prefix=(1,2,4), pos=4, S=(1,2,3,4)
                        # thus delete the states like (1,2,4,3)
        cur = S[i]
#        prefix.append(cur)
        generateSubset(S, prefix+[cur], i+1)
#        prefix.pop()


S = [1,2,3,4]
generateSubset(S, [], 0)
