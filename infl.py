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
- `prch(nnnn:int)->bool`: checks if a number is a registered prime.
'''
import sys
import primes
NNNN = 32771


def prch(nnnn: int) -> bool:
    '''
    Checks if a number is a registered prime.
    '''
    return nnnn in primes.p


def infl(prim: int, snum: int, nnnn: int = NNNN) -> int:
    '''
    Initializes fields.
    `1 < prim`: Primitive form of the word.
    `0 < snum`: Serial number of the inflection.
    '''
    return prim**snum % nnnn


if __name__ == '__main__':
    for a in range(2, NNNN):
        m = set()
        l = 0
        for b in range(1, NNNN):
            n = infl(a, b, NNNN)
            m.add(n)
            l += 1
            if l != len(m):
                print(f'{a}**{b}: {n}')
                break
