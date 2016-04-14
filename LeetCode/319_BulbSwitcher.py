def bulbSwitch(n):
    """
    :type n: int
    :rtype: int
    """
    bulbs  = [0 for i in range(n)]
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i % j == 0: # j is i's factor
                bulbs[i-1] = 1 - bulbs[i-1]
    return sum(bulbs)

def tricky_bulbSwitch(n):
    import math
    return int(math.sqrt(n))
