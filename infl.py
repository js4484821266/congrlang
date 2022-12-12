'''
Generator for the inflections.
'''


def infl(prim: int, snum: int, nnnn: int) -> int:
    '''
    Initializes fields.
    `prim`: Primitive form of the word.
    `snum`: Serial number of the inflection.
    `nnnn`: Divisor of the modulo operation.
    '''
    return prim**snum % nnnn


if __name__ == '__main__':
    print(infl(7, 7, 101))
