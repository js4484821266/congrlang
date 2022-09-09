import re
import congrlang


def evaluate(vrb: str) -> int:
    sum = 0
    wei = 1
    pnm = [0, 0, 0]
    xcl = f'[^{"".join(congrlang.HEAD+congrlang.VOWEL)}]'
    while vrb:
        hhh = [i for i in congrlang.HEAD if i != pnm[2]]
        vrx = f'({"|".join(congrlang.VOWEL)})'
        hrx = f'({"|".join(hhh)})'
        pnm[1] = re.search(vrx, vrb, re.I)
        if not pnm[1]:
            break
        pnm[0] = re.search(hrx, vrb[:pnm[1].start()], re.I)
        try:
            pnm[0] = pnm[0].group()
        except:
            pass
        vrb = vrb[pnm[1].end():]
        pnm[1] = pnm[1].group()
        try:
            vrb = vrb[re.search(xcl+f'({pnm[1]})*').end():]
        except:
            pass
        try:
            pnm[2] = re.search(
                xcl +
                f'({"|".join(i for i in congrlang.TAIL if i)})' +
                f'(?!{"|".join(congrlang.VOWEL)})',
                vrb, re.I
            )
            vrb = vrb[pnm[2].end():]
            pnm[2] = pnm[2].group()
        except:
            pass
        pnm = [0, 0, 0]
    return sum+1


if __name__ == '__main__':
    print(evaluate('        m44488tchtcthccaaapaaaaiaiaiaaaaa884i   04022p'))
