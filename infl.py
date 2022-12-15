'''
Generator of the inflections.

Suppose there is a congruence equation:
`m=a**b%N`
where
- `m` is the inflection,
- `a` is the primitive form of the word,
- `b` is the serial number of the inflection, and
- `N` is the divisor, the constant.

Constants:
- `NNNN`: `N` of the equation above.
- `PRMX`: maximum of the primitive form of the words.
- `SNMX`: maximum of the serial number of the inflections.

Functions:
- `infl(prim:int,snum:int)->int`: returns the inflection, `prim**snum%NNNN`
'''
import sys
NNNN = 1073741827
PRMX = 2**20
SNMX = NNNN/PRMX


def infl(prim: int, snum: int) -> int:
    '''
    Initializes fields.
    `1 < prim < PRMX`: Primitive form of the word.
    `0 < snum < SNMX`: Serial number of the inflection.
    '''
    if 1 >= prim or prim >= PRMX:
        raise ValueError(f'supposed to be 1 < prim < {PRMX}')
    if 0 >= snum or snum >= SNMX:
        raise ValueError(f'supposed to be 0 < snum < {SNMX}')
    return prim**snum % NNNN


if __name__ == '__main__':
    a = int(sys.argv[1])
    b = 1
    m = set()
    l = 0
    while True:
        n = infl(a, b)
        print(f'{b}: {n}')
        b += 1
        l = len(m)
        m.add(n)
        if l == len(m):
            break
