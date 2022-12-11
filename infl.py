'''
Universal inflector source code for every version of Congrlang.
'''


class Phrs:
    '''
    Defines an object of a phrase.
    '''

    def __init__(self) -> None:
        pass


def infl(prim: int, snum: int, nnnn: int) -> int:
    '''
    Initializes fields.
    `prim`: Primitive form of the word.
    `snum`: Serial number of the inflection.
    `nnnn`: Divisor of the modulo operation.
    '''
    return prim**snum % nnnn


def sntn(subj: int, prdc: int, advb: dict[int, int]) -> int:
    '''
    Initializes fields.
    `subj`: The subject.
    `prdc`: The predicate.
    `advb`: The adverbial phrases.
    '''
    pppp = []
    with open('primes.txt', 'r', encoding='646')as ptxt:
        pppp = list(map(int, ptxt.read().split()))

    # TODO
if __name__ == '__main__':
    pass
