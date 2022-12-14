'''
Generator of the inflections.
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
