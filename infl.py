'''
Universal inflector source code for every version of Congrlang.
'''


class Infl:
    '''
    Defines an object of an inflection.
    '''

    def __init__(self,
                 prim: int,
                 infl: int
                 ) -> None:
        '''
        Initializes fields.
        `prim`: Primitive form of the word.
        `infl`: Serial number of the inflection.
        '''
        self.prim = prim
        self.infl = infl

    def set(self,
            prim: int,
            infl: int
            ) -> None:
        '''
        Initializes fields.
        `prim`: Primitive form of the word.
        `infl`: Serial number of the inflection.
        '''
        self.prim = prim
        self.infl = infl


class Sntn:
    '''
    Defines an object of a sentence.
    '''

    def __init__(self,
                 abso: int,
                 verb: int
                 ) -> None:
        '''
        Initializes fields.
        `abso`: The noun in the absolutive case.
        `verb`: The verb.
        '''
        self.abso = abso
        self.verb = verb

    def set(self,
            abso: int,
            verb: int
            ) -> None:
        '''
        Initializes fields.
        `abso`: The noun in the absolutive case.
        `verb`: The verb.
        '''
        self.abso = abso
        self.verb = verb


if __name__ == '__main__':
    pass
