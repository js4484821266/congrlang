import itertools as it
import re

import congrlang


def syllable_analysis(lem: str) -> "list[str]":
    vrc = re.compile(
        f'({"|".join(sorted(congrlang.VOWEL,key=len,reverse=True))})',
        re.I)
    # vowels regex compiled
    hrc = re.compile(
        f'({"|".join(sorted([i for i in congrlang.HEAD if i],key=len,reverse=True))})',
        re.I)
    # head consonants regex compiled
    vwl = list(vrc.finditer(lem))
    # list of match object of vowels
    if not vwl:
        return []  # no vowels -> no syllables
    for i in range(1,len(vwl)):
        try:
            pass
        except:
            pass

    opn = []
    # opening consonant
    clo = []
    # closing consonant
    for iii in range(len(vwl) + 1):
        cons = []
        # list of consonants between vowels
        if iii == 0:
            cons.extend(hrc.finditer(lem, 0, vwl[iii].start()))
        elif iii == len(vwl):
            cons.extend(hrc.finditer(lem, vwl[iii - 1].end(), len(lem)))
        else:
            cons.extend(hrc.finditer(
                lem, vwl[iii - 1].end(), vwl[iii].start()))
        # push consonants

        tail = list(it.takewhile(lambda x: x.group() in congrlang.TAIL, cons))
        clo.append(None if len(cons) <= 1 or len(tail) == 0 else cons[0])
        opn.append(None if not len(cons) else cons[-1])

    clo = clo[1:]
    syl = []
    for i in range(len(vwl)):
        syl.append(('' if not opn[i] else opn[i].group()) +
                   ('' if not vwl[i] else vwl[i].group()) +
                   ('' if not clo[i] else clo[i].group()))
    
    return syl


def evaluate(lem: str) -> int:
    sum = 0
    syl = syllable_analysis(lem)
    # TODO
    return sum+1


if __name__ == '__main__':
    lem = 'pannamaan'
    print(syllable_analysis(lem))
    # print(evaluate(lem))
