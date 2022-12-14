'''
primes
'''
p = []


def defp():
    '''
    Generates p.
    '''
    global p
    if not p:
        with open('primes.txt', 'r', encoding='646') as r:
            p = list(map(int, r.read().split()))


def nxpr():
    '''
    the next prime?
    '''
    defp()
    inon = p[-1]
    while True:
        inon += 2
        for jjjj in p:
            if not inon % jjjj:
                break
            if jjjj*jjjj > inon:
                return inon


def papp() -> None:
    '''
    appends nxpr to p.
    '''
    defp()
    prim = nxpr()
    if prim in p:
        return
    p.append(prim)


if __name__ == '__main__':
    defp()
    print(p[-1])
    import time
    import threading
    thrs = []
    t0 = time.time()
    try:
        for i in range(16):
            t = threading.Thread(target=papp)
            t.start()
            print(f'Thr {t.ident} started.')
            thrs.append(t)
        while True:
            for t in thrs:
                if t.is_alive():
                    continue
                t.join()
                if time.time()-t0 >= 1:
                    print(p[-1])
                    t0 = time.time()
                t = threading.Thread(target=papp)
                t.start()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        for t in thrs:
            print(f'Thr {t.ident} ', end='')
            t.join()
            print('disconnected.')
    P = sorted(set(p))
    print(P[-1])
    with open('primes.txt', 'w', encoding='646') as w:
        w.write('\n'.join(map(str, P)))
