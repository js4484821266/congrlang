'''
Euler's totient function.
'''
import primefactorizer

q = []
with open('phi.txt', 'r', encoding='646') as r:
    q = set(enumerate(map(int, r.read().split())))


def phii(xxxx: int) -> int:
    '''
    Euler's totient function.
    '''
    pwfc = primefactorizer.ftrz(xxxx)
    phpx = 1
    for ppjj, xfjj in pwfc:
        prxp = ppjj**xfjj
        phpx *= prxp-prxp//ppjj
    return phpx


def qadd() -> None:
    '''
    appends a key-value pair to q.
    '''
    lenq = len(q)
    q.add((lenq,phii(lenq)))


if __name__ == '__main__':
    print(len(q))
    import time
    import threading
    thrs = []
    t0 = time.time()
    try:
        for i in range(16):
            t = threading.Thread(target=qadd)
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
                t = threading.Thread(target=qadd)
                t.start()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        for t in thrs:
            print(f'Thr {t.ident} ', end='')
            t.join()
            print('disconnected.')
    print(len(q))
    with open('phi.txt', 'w', encoding='646') as w:
        i = sorted(q, key=lambda x: x[0])
        i = map(lambda x: str(x[1]), i)
        i = list(i)
        w.write('\n'.join(i))
