HEAD = ['', 'm', 'p', 'f', 't', 's', 'q', 'c', 'k',
        'h', 'n', 'l',  'r']
VOWEL = ['i', 'u', 'e', 'y', 'o', 'a']
TAIL = ['', 'p', 'f',  's', 'c', 'h', 'n', 'l', 'r']
for i in TAIL:
    if i not in HEAD:
        raise ValueError
if __name__ == '__main__':
    s = []
    for i in VOWEL:
        for j in HEAD:
            for k in TAIL:
                s.append(j+i+k)
    print(s)
    print(len(s))
