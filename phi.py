'''
Euler's totient function.
'''
import time
import primes

q = []
with open('phi.txt', 'r', encoding='646') as f:
    q = list(map(int, f.read().split()))
if __name__ == '__main__':
    with open('phi.txt', 'w', encoding='646') as f:
        i = len(q)
        print(i)
        t0 = time.time()
        try:
            while primes.p[-1] > i:
                t = []
                k = i
                for j in primes.p:
                    if j*j > i:
                        break
                    t.append(0)
                    while k>1 and not k % j:
                        t[-1] += 1
                        k //= j
                u = 1
                for pj,tj in zip(primes.p,t):
                    v=pj**tj
                    u*=v-v//pj
                q.append(u)
                if not i % 1000:
                    t1 = time.time()
                    print(f'{i}: {t1-t0}s')
                    t0 = t1
                i += 1
        except KeyboardInterrupt:
            print(i)
        f.write(' '.join(map(str, q)))
