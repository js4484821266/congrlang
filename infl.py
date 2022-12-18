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
- `infl(prim:int,snum:int)->int`:
  returns the inflection, `prim**snum%NNNN`
'''
import nnnn


def infl(prim: int, snum: int, modn: int = nnnn.N) -> int:
    '''
    Initializes fields.
    `1 < prim`: Primitive form of the word.
    `0 < snum`: Serial number of the inflection.
    '''
    return prim**snum % modn


if __name__ == '__main__':
    for a in range(2, nnnn.N):
        m = set()
        l = 0
        for b in range(1, nnnn.N):
            n = infl(a, b, nnnn.N)
            m.add(n)
            l += 1
            if l != len(m):
                print(f'{a}**{b}: {n}')
                break
