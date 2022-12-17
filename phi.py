'''
Euler's totient function.
'''
import time
import primes

q = []
with open('phi.txt', 'r', encoding='646') as f:
    q = list(map(int, f.read().split()))
if __name__ == '__main__':
    with open('phi.txt', 'a', encoding='646') as f:
        i = len(q)
        print(i)
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
                i += 1
        except KeyboardInterrupt:
            print(i)
