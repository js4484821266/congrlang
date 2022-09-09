import re
import congrlang


def evaluate(word: str) -> int:
    sum = 0
    weight = 1
    phonemes = [0, 0, 0]
    excluded = f'[^{"".join(congrlang.HEAD+congrlang.VOWEL)}]'
    while word:
        headsnow = [i for i in congrlang.HEAD if i and i != phonemes[2]]
        vowelregex = f'({"|".join(congrlang.VOWEL)})'
        headregex = f'({"|".join(headsnow)})'
        phonemes[1] = re.search(vowelregex, word, re.I)
        if not phonemes[1]:
            break
        phonemes[0] = re.search(headregex, word[:phonemes[1].start()], re.I)
        try:
            phonemes[0] = phonemes[0].group()
        except:
            pass
        word = word[phonemes[1].end():]
        phonemes[1] = phonemes[1].group()
        try:
            word = word[re.search(excluded+f'({phonemes[1]})*').end():]
        except:
            pass
        try:
            phonemes[2] = re.search(
                excluded +
                f'({"|".join(i for i in congrlang.TAIL if i)})' +
                f'(?!{"|".join(congrlang.VOWEL)})',
                word, re.I
            )
            word = word[phonemes[2].end():]
            phonemes[2] = phonemes[2].group()
        except:
            pass
        phonemes = [0, 0, 0]
    return sum+1


if __name__ == '__main__':
    print(evaluate('        m44488tchtcthccaaapaaaaiaiaiaaaaa884i   04022p'))
