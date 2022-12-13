'''
Generator for the inflections.
'''
import sys
NNNN = 1073741827
PRMX=2**20
SNMX=NNNN//PRMX

def infl(prim: int, snum: int) -> int:
    '''
    Initializes fields.
    `1 < prim < PRMX`: Primitive form of the word.
    `0 < snum < SNMX`: Serial number of the inflection.
    '''
    if 1 >= prim or prim >= PRMX:
        eeee=f'1 < prim < {PRMX}'
        raise ValueError(eeee)
    if 0 >= snum or snum >= NNNN/PRMX:
        eeee=f'0 < snum < {SNMX}'
        raise ValueError(eeee)
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
