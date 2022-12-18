'''
helps designate N.
'''
import primes
import phi
N = 0
M = 0
r = len(primes.p)
p = ()
for i in primes.p:
    try:
        j = phi.q[i-1]/phi.q[i]
        k = phi.q[i+1]/phi.q[i]
        if j < r:
            N = i
            M = i-1
            r = j
        if k < r:
            N = i
            M = i+1
            r = k
        p=(N, M, r)
    except IndexError:
        break
if __name__ == '__main__':
    print(p)
