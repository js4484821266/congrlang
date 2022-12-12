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
