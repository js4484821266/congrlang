'''
primes
'''
import time
p = []
with open('primes.txt', 'r', encoding='646') as f:
    p = sorted(list(map(int, f.read().split())))
if __name__ == '__main__':
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
                if i % 1000 == 1:
                    t001 = time.time()
                    print(f'{i}: {t001-t000}s')
                    t000 = t001
        except KeyboardInterrupt:
            print(p[-1])
        f.write(' '.join(map(str, p)))
