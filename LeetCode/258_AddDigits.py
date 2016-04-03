def addDigits(num):
    if num < 10: return num
    next = 0
    while num > 0:
        next += num % 10
        num /= 10
    return self.addDigits(next)
    
