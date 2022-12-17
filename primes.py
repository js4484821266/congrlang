'''
primes
'''
import math
import time
p = []
with open('primes.txt', 'r', encoding='646') as f:
    p = sorted(list(map(int, f.read().split())))
if __name__ == '__main__':
    ml1d=math.log(1.1)
    with open('primes.txt', 'w', encoding='646') as f:
        i = p[-1]
        print(i)
        t000 = time.time()
        try:
            while True:
                i += 2
                for j in p+[0]:
                    if j > 1 and not i % j:
                        break
                    elif not j:
                        p.append(i)
                    else:
                        pass
                if int(math.log(i)/ml1d)>int(math.log(i-1)/ml1d):
                    t001 = time.time()
                    print(f'{i}: {int((t001-t000)*1000)}ms')
                    t000 = t001
        except KeyboardInterrupt:
            print(p[-1])
        f.write(' '.join(map(str, p)))
