'''
Designates N.
'''
import primes
import phi
N = 0
r = 9
for i in primes.p[1:]:
    try:
        j = phi.q[i]/phi.q[phi.q[i]]
        if j <= r:
            N = i
            r = j
            # TODO
    except IndexError:
        break
if __name__ == '__main__':
    print(N, r)
