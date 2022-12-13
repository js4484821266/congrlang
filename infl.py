'''
Generator for the inflections.
'''

NNNN = 2147483647


def infl(prim: int, snum: int) -> int:
    '''
    Initializes fields.
    `1 < prim < 2**20`: Primitive form of the word.
    `0 < snum < 2**11`: Serial number of the inflection.
    '''
    if 1 >= prim or prim >= 2**20:
        raise ValueError("1 < prim < 2**20")
    if 0 >= snum or snum >= 2**11:
        raise ValueError("0 < prim < 2**11")
    return prim**snum % NNNN


if __name__ == '__main__':
    a = 4
    b = 1
    m = set()
    l=0
    while True:
        n = infl(a, b)
        print(f'{b}: {n}')
        b+=1
        l=len(m)
        m.add(n)
        if l==len(m):
            break