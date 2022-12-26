'''
Factorization.
'''
import primes


def ftrz(intn: int) -> set[tuple[int, int]]:
    '''
    Factorization.
    '''
    primes.defp()
    if intn > primes.p[-1]**2:
        raise ValueError(
            "argument greater than"
            + "the greatest registered prime"
        )
    pwfc = set()
    for pppp in primes.p:
        tttt = {pppp: 0}
        while not intn % pppp:
            intn //= pppp
            tttt[pppp] += 1
        if tttt[pppp]:
            pwfc.update(tttt.items())
        if intn == 1:
            break
    return pwfc


if __name__ == '__main__':
    print(ftrz(2*3*5*7*11*13*17*19*23))
