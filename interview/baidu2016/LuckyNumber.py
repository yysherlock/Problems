astr, bstr = raw_input().split()
a = int(astr)
b = int(bstr)

ln = set({'4','7'})
cur = a + 1
while True:
    s = ''
    for c in str(cur):
        if c in ln:
            s += c
    if bstr in s:
        print cur
        break
    cur += 1
