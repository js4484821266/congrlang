'''
primes
'''
p = []
with open('primes.txt', 'r', encoding='646') as r:
    p = list(map(int, r.read().split()))


def nxpr():
    '''
    the next prime?
    '''
    while True:
        inon = p[-1]
        inon += 2
        for jjjj in p+[0]:
            if jjjj**2 > inon:
                break
            if jjjj > 1 and not inon % jjjj:
                break
            if not jjjj:
                return inon


def papp() -> None:
    '''
    appends nxpr to p.
    '''
    prim = nxpr()
    if prim in p:
        return
    else:
        p.append(prim)


if __name__ == '__main__':
    print(p[-1])
    import threading
    nthr = 8
    thrs = list()
    try:
        for i in range(nthr):
            t = threading.Thread(target=papp, daemon=True)
            t.start()
            thrs.append(t)
        while True:
            for t in range(nthr):
                if thrs[t].is_alive():
                    continue
                thrs[t].join()
                print(f'Thread {t}... {p[-1]}')
                thrs[t] = threading.Thread(target=papp)
                thrs[t].start()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        for t in thrs:
            t.join()
    P = sorted(set(p))
    print(P[-1])
    with open('primes.txt', 'w', encoding='646') as w:
        w.write('\n'.join(map(str, P)))
