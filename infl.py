'''
Universal inflector source code for every version of Congrlang.
'''


class Infl:
    '''
    Defines an object of an inflection.
    '''

    def __init__(self,
                 prim: int,
                 infl: int,
                 nnnn: int
                 ) -> None:
        '''
        Initializes fields.
        `prim`: Primitive form of the word.
        `infl`: Serial number of the inflection.
        `nnnn`: Divisor of the modulo operation.
        '''
        self.prim = prim
        self.infl = infl
        self.nnnn = nnnn

    def set(self,
            prim: int,
            infl: int,
            nnnn: int
            ) -> None:
        '''
        Initializes fields.
        `prim`: Primitive form of the word.
        `infl`: Serial number of the inflection.
        `nnnn`: Divisor of the modulo operation.
        '''
        self.prim = prim
        self.infl = infl
        self.nnnn = nnnn

    def out(self) -> int:
        '''
        Returns the inflection.
        '''
        return self.prim**self.infl % self.nnnn


class Sntn:
    '''
    Defines an object of a sentence.
    '''

    def __init__(self,
                 subj: int,
                 verb: int,
                 advb: dict[int, int]
                 ) -> None:
        '''
        Initializes fields.
        `subj`: The subject.
        `verb`: The verb.
        `advb`: The adverbial phrases.
        '''
        self.subj = subj
        self.verb = verb
        self.advb = advb

    def set(self,
            subj: int,
            verb: int,
            advb: dict[int, int]
            ) -> None:
        '''
        Initializes fields.
        `subj`: The subject.
        `verb`: The verb.
        `advb`: The adverbial phrases.
        '''
        self.subj = subj
        self.verb = verb
        self.advb = advb


if __name__ == '__main__':
    pass
