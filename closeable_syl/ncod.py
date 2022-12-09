import congrlang


def encode(n: int) -> str:
    s = ""
    q = n-1
    while q > 0:
        r = q % congrlang.n
        q = q//congrlang.n
    return s


if __name__ == '__main__':
    print(encode(11))
