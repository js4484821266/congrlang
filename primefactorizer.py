'''
Factorization.
'''
import primes
def ftrz(intn:int)->dict[int,int]:
    '''
    Factorization.
    '''
    pwfc=dict()
    for pppp in primes.p:
        pwfc[pppp]=0
        while not intn%pppp:
            intn//=pppp
            pwfc[pppp]+=1
        if not pwfc[pppp]:
            del pwfc[pppp]
        if intn==1:
            break
    return pwfc
if __name__=='__main__':
    print(ftrz(2*3*5*7*9*11*17))