import re
import congrlang


def evaluate(x: str) -> int:
    v = 0
    w = 1
    p = [0, 0, 0]
    xc=f'[^{"".join(set(congrlang.HEAD+congrlang.VOWEL))}]'
    while x:
        hh = [i for i in congrlang.HEAD if i and i != p[2]]
        vr = f'({"|".join(congrlang.VOWEL)})'
        hr = f'({"|".join(hh)})'
        p[1] = re.search(vr, x, re.I)
        if not p[1]:
            break
        p[0] = re.search(hr, x[:p[1].start()], re.I)
        try:
            p[0] = p[0].group()
        except:
            pass
        x = x[p[1].end():]
        p[1] = p[1].group()
        x = re.sub(f'{p[1]}*', '', x, count=1)
        try:
            p[2] = re.search(
                f'[^{vr+"|"+"|".join(congrlang.HEAD_ONLY)}]*' +
                f'({"|".join(i for i in congrlang.TAIL if i)})' +
                f'(?!{"|".join(congrlang.VOWEL)})',
                x, re.I
            )
            x = x[p[2].end():]
            p[2] = p[2].group()
        except:
            pass
        p = [0, 0, 0]
    return v+1


if __name__ == '__main__':
    print(evaluate('        m44488tchtcthccaaapaaaaiaiaiaaaaa884i   04022p'))
