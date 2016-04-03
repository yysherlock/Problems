
# Time limited version

def canWinNim(n):
    if n==1 or n==2 or n==3: return True
    return (not canWinNim(n-1)) or (not canWinNim(n-2)) or (not canWinNim(n-3))

print canWinNim(4), canWinNim(30)
# print canWinNim1(38) # time limit

def tricky_canWinNim(n):
    return not n % 4 == 0
print tricky_canWinNim(38)
