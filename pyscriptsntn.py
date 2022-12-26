from pyscript import Element


def sntn():
    xxxx = 0
    dddd = dict()
    idid = ['vbab', 'vbnn', 'erab', 'ernn', 'abab', 'abnn']
    for i in idid:
        dddd[i] = int(Element(i).value)
    mmmm = 1
    for id in idid[1::2]:
        mmmm *= dddd[id]
    for id, ab in zip(idid[1::2], idid[::2]):
        n = mmmm//dddd[id] % dddd[id]
        s = 1
        while n*s % dddd[id] != 1:
            s += 1
        xxxx += ab*n*s
    Element('sntn').write(xxxx)
