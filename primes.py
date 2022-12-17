'''
primes
'''
import math
import time
p = []
with open('primes.txt', 'r', encoding='646') as f:
    p = sorted(list(map(int, f.read().split())))
if __name__ == '__main__':
    mlb = math.log(1.01)
    with open('primes.txt', 'w', encoding='646') as f:
        i = p[-1]
        print(i)
        t0 = time.time()
        try:
            while True:
                i += 2
                for j in p+[0]:
                    if j > 1 and not i % j:
                        break
                    if not j:
                        p.append(i)
                t1 = time.time()
                if t1-t0 >= 1:
                    print(i)
                    t0 = t1
        except KeyboardInterrupt:
            print(p[-1])
        f.write('\n'.join(map(str, p)))
