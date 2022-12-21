'''
Euler's totient function.
'''
import primefactorizer

q = []
with open('phi.txt', 'r', encoding='646') as r:
    q = list(map(int, r.read().split()))
    q = dict(enumerate(q))


def phii(xxxx: int = len(q)) -> int:
    '''
    Euler's totient function.
    '''
    pwfc = primefactorizer.ftrz(xxxx)
    phab = 1
    for ppjj, xfjj in pwfc.items():
        phpe = ppjj**xfjj
        phab *= phpe-phpe//ppjj
    return phab


def qipi(indx: int = len(q)) -> None:
    '''
    appends a key-value pair to q.
    '''
    q[indx] = phii(indx)


if __name__ == '__main__':
    print(len(q))
    import time
    import threading
    thrs = []
    t0 = time.time()
    try:
        for i in range(32):
            t = threading.Thread(target=qipi)
            t.start()
            print(f'Thr {t.ident} started.')
            thrs.append(t)
        while True:
            for t in thrs:
                if t.is_alive():
                    continue
                t.join()
                if time.time()-t0 >= 1:
                    print(len(q))
                    t0 = time.time()
                t = threading.Thread(target=qipi)
                t.start()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        for t in thrs:
            print(f'Thr {t.ident} ', end='')
            t.join()
            print('disconnected.')
    print(len(q))
    with open('phi.txt', 'w', encoding='646') as w:
        i = q.items()
        i = sorted(i, key=lambda x: x[0])
        i = map(lambda x: str(x[1]), i)
        i = list(i)
        w.write('\n'.join(i))
