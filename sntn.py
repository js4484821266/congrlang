'''
Universal inflector source code for every version of Congrlang.
'''
import infl


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
