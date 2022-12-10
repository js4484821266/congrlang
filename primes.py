'''
primes
'''
import math
p = []
if __name__ == '__main__':
    with open('primes.txt', 'r', encoding='646') as f:
        p = sorted(list(map(int, f.read().split(','))))
    r=int(math.log(p[-1],1.001))
    with open('primes.txt', 'w', encoding='646') as f:
        i = p[-1]+2
        print(r)
        try:
            while True:
                for j in p+[0]:
                    if j > 1 and not (i % j):
                        break
                    elif not j:
                        p.append(i)
                    else:
                        pass
                l=int(math.log(i,1.001))
                if l!=r:
                    r=l
                    print(r)
                i += 2
        except KeyboardInterrupt:
            print(p[-1])
        f.write(','.join(map(str, p)))
