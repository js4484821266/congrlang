import re
import congrlang


def syllable_analysis(lem: str) -> list[str]:
    vrc = re.compile(
        f'({"|".join(sorted(congrlang.VOWEL,key=lambda x:len(x),reverse=True))})',
        re.I)
    # vowels regex compiled
    hrc = re.compile(
        f'({"|".join(sorted([i for i in congrlang.HEAD if i],key=lambda x:len(x),reverse=True))})',
        re.I)
    # head consonants regex compiled
    vwl = [re.search('', '')]
    # Match objects of syllables
    while vwl[-1]:
        vwl.append(vrc.search(lem, vwl[-1].end()))
        # list of match object of vowels
    if len(vwl) <= 2:
        return []
    iii = 1
    opn = []
    # opening
    clo = []
    # closing
    while vwl[iii]:
        # filtering consonants
        hhh = [vwl[iii-1]]
        # list of consonants between vowels
        while hhh[-1]:
            hhh.append(hrc.search(lem, hhh[-1].end(), vwl[iii].start()))
            # push consonants
        iii += 1
        try:
            ttt = [i for i in hhh[1:-1] if i.group() in congrlang.TAIL]
            clo.append(ttt[0]if hhh[-2].group() != ttt[0].group()else None)
        except:
            clo.append(None)
        opn.append(hhh[-2])
    clo.append(re.compile(f'({"|".join(i for i in congrlang.TAIL if i)})').search(
        lem, vwl[-2].end()))
    syl = []
    for i in range(len(vwl)-2):
        syl.append((''if not opn[i] else opn[i].group()) +
                   (''if not vwl[i+1]else vwl[i+1].group()) +
                   (''if not clo[i+1]else clo[i+1].group()))
    return syl


def evaluate(lem: str) -> int:
    sum = 0
    syl = syllable_analysis(lem)
    return sum+1


if __name__ == '__main__':
    print(syllable_analysis('anata no haato ni niko niko ni'))