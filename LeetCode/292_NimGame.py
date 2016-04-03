
# Time limited version

def canWinNim1(n):
    if n==1 or n==2 or n==3: return True
    return (not canWinNim1(n-1)) or (not canWinNim1(n-2)) or (not canWinNim1(n-3))

print canWinNim1(4), canWinNim1(30)
# print canWinNim1(38) # time limit

def canWinNim(n):
    return not n % 4 == 0
print canWinNim(38)
