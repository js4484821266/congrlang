'''
primes
'''
p = [2, 3, 5, 7]
if __name__ == '__main__':
    with open('primes.txt', 'a+', encoding='646') as f:
        p=list(map(int,f.read().split('\n')))
        i = p[-1]+2
        while i < 1000000:
            for j in p+[0]:
                if j > 1 and not (i % j):
                    break
                elif not j:
                    p.append(i)
                    print(i)
                else:
                    pass
            i += 2
