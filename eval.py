import re
import congrlang


def evaluate(lem: str) -> int:
    sum = 0  # sum
    wei = 1  # weight
    vrx = re.compile(f'({"|".join(congrlang.VOWEL)})')  # vowels regex
    syl = [re.search('','')]  # position of syllables
    while syl[-1]:
        syl.append(vrx.search(lem,pos=syl[-1].end()))
    syl=syl[1:-1]
    return sum+1


if __name__ == '__main__':
    print(evaluate('11100a8288222     e   io  u555'))
