import re
import cngr as C


def eval(word: str) -> int:
    y = 0
    w=re.findall(
        '['+''.join(C.C+C.V)+']?',
        word,
        re.I
    )
    
    # TODO
    return y


if __name__ == '__main__':
    print(eval('cdsfcsdfscf22222cdfqqq'))
