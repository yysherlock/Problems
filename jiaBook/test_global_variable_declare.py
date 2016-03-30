
tot = 0

def test_local_refvar():
    global tot # if you want to change global tot inside function, you should declare it as global.
    print tot
    tot += 1
    print tot

test_local_refvar()
