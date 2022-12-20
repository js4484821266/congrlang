'''
primes
'''
p = []
with open('primes.txt', 'r', encoding='646') as r:
    p = list(map(int, r.read().split()))


def nxpr(inon: int = p[-1]):
    '''
    the next prime?
    - `inon`: initial odd number
    '''
    while True:
        inon += 2
        for jjjj in p+[0]:
            if jjjj > 1 and not inon % jjjj:
                break
            if not jjjj:
                return inon


def papp(inon: int = p[-1])->None:
    '''
    appends nxpr to p.
    '''
    prim = nxpr(inon)
    if prim in p:
        return
    else:
        p.append(prim)


if __name__ == '__main__':
    print(p[-1])
    import threading
    thrs = list()
    import time
    t0=time.time()
    try:
        for i in range(10):
            t=threading.Thread(target=papp)
            t.start()
            thrs.append(t)
        while True:
            for t in thrs:
                t1=time.time()
                if t.is_alive():
                    continue
                else:
                    t.join()
                # TODO
                t=threading.Thread(target=papp)
                t.start()
    except KeyboardInterrupt:
        for t in thrs:
            t.join()
    P=sorted(set(p))
    print(P[-1])
    with open('primes.txt', 'w', encoding='646') as w:
        w.write('\n'.join(map(str, P)))
