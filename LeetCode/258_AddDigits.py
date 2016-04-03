def addDigits(num):
    if num < 10: return num
    next = 0
    while num > 0:
        next += num % 10
        num /= 10
    return addDigits(next)

def tricky_addDigits(num):
    if num < 10: return num
    re = num % 9
    if re: return re
    else: return 9
