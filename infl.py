'''
Generator of the inflections.

Suppose there is a congruence equation:
`m=a**b%N`
where
- `m` is the inflection,
- `a` is the primitive form of the word,
- `b` is the serial number of the inflection, and
- `N` is the divisor, the constant.

Functions:
- `infl(prim:int,snum:int)->int`: returns the inflection, `prim**snum%NNNN`
'''
import sys
import primes


def infl(prim: int, snum: int, nnnn: int) -> int:
    '''
    Initializes fields.
    `1 < prim`: Primitive form of the word.
    `0 < snum`: Serial number of the inflection.
    '''
    return prim**snum % nnnn


if __name__ == '__main__':
    a = int(sys.argv[1])
    b = 1
    m = set()
    l = 0
    while True:
        n = infl(a, b, 1073741827)
        print(f'{b}: {n}')
        b += 1
        l = len(m)
        m.add(n)
        if l == len(m):
            break
