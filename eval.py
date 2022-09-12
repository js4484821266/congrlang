import re
import itertools as it
import congrlang


def syllable_analysis(lem: str)-> "list[str]":
    vrc = re.compile(
        f'({"|".join(sorted(congrlang.VOWEL,key=len,reverse=True))})',
        re.I)
    # vowels regex compiled
    hrc = re.compile(
        f'({"|".join(sorted([i for i in congrlang.HEAD if i],key=len,reverse=True))})',
        re.I)
    # head consonants regex compiled
    vowel = list(vrc.finditer(lem))
    # list of match object of vowels
    if not vowel:
        return [] # no vowels -> no syllables

    opn = []
    # opening consonant
    clo = []
    # closing consonant
    for iii in range(len(vowel) + 1):
        cons = []
        # list of consonants between vowels
        if iii == 0:
            cons.extend(hrc.finditer(lem, 0, vowel[iii].start()))
        elif iii == len(vowel):
            cons.extend(hrc.finditer(lem, vowel[iii - 1].end(), len(lem)))
        else:
            cons.extend(hrc.finditer(lem, vowel[iii - 1].end(), vowel[iii].start()))
        # push consonants

        tail = list(it.takewhile(lambda x: x.group() in congrlang.TAIL, cons))
        if len(cons) == 0:
            clo.append(None)
            opn.append(None)
        elif len(cons) == 1:
            clo.append(None)
            opn.append(cons[0])
        elif len(cons) == 2:
            if len(tail) >= 1:
                clo.append(cons[0])
                opn.append(cons[-1])
            else:
                raise ValueError
        else:
            raise ValueError

    syl = []
    for i in range(len(vowel)):
        syl.append(('' if not opn[i] else opn[i].group()) +
                   ('' if not vowel[i] else vowel[i].group()) +
                   ('' if not clo[i] else clo[i].group()))
    return syl   


def evaluate(lem: str) -> int:
    sum = 0
    return sum+1


if __name__ == '__main__':
    print(evaluate('anata no haato ni niko niko ni'))
