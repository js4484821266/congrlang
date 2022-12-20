'''
Euler's totient function.
'''
import primes

q = []
with open('phi.txt', 'r', encoding='646') as f:
    q = list(map(int, f.read().split()))
    q = dict(enumerate(q))


def phii(xxxx: int) -> int:
    '''
    Euler's totient function.
    '''
    pwfc = []
    for pppp in primes.p:
        pwfc.append(0)
        while not xxxx % pppp:
            pwfc[-1] += 1
            xxxx //= pppp
        if xxxx == 1:
            break
    phab = 1
    for ppjj, xfjj in zip(primes.p, pwfc):
        phpe = ppjj**xfjj
        phab *= phpe-phpe//ppjj
    return phab


def qipi(indx: int) -> None:
    '''
    appends a key-value pair to q.
    '''
    q[indx] = phii(indx)


if __name__ == '__main__':
    i = len(q)
    print(i)
    import time
    t0 = time.time()
    try:
        while primes.p[-1] > i:
            t = []
            k = i
            for j in primes.p:
                t.append(0)
                while not k % j:
                    t[-1] += 1
                    k //= j
                if k == 1:
                    break
            u = 1
            for pj, tj in zip(primes.p, t):
                v = pj**tj
                u *= v-v//pj
            f.write(f'\n{u}')
            t1 = time.time()
            if t1-t0 >= 1:
                print(i)
                t0 = t1
    except KeyboardInterrupt:
        print(i)
    with open('phi.txt', 'a', encoding='646') as f:
        pass
    # TODO
