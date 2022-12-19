'''
primes
'''
import time
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
        dlep=0
        for jjjj in p+[0]:
            if jjjj > 1 and not inon % jjjj:
                break
            if not jjjj:
                p.append(inon)
                dlep=1
        if dlep:
            break
        


if __name__ == '__main__':
    print(p[-1])
    t0 = time.time()
    try:
        nxpr()
        t1 = time.time()
        if t1-t0 >= 1:
            print(p[-1])
            t0 = t1
    except KeyboardInterrupt:
        pass
    print(p[-1])
    with open('primes.txt', 'w', encoding='646') as w:
        w.write('\n'.join(map(str, sorted(set(p)))))
