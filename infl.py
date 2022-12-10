'''
Universal inflector source code for every version of Congrlang.
'''


class Infl:
    '''
    Defines an object of an inflection.
    '''

    def __init__(self,
                 prim=1,
                 infl=1
                 ) -> None:
        '''
        Initializes fields.
        `prim`: Primitive form of the word.
        `infl`: Serial number of the inflection.
        '''
        self.prim = prim
        self.infl = infl

    def set(self,
            prim=1,
            infl=1
            ) -> None:
        '''
        Initializes fields.
        `prim`: Primitive form of the word.
        `infl`: Serial number of the inflection.
        '''
        self.prim = prim
        self.infl = infl


class Sntx:
    '''
    Defines an object of a sentence.
    '''

    def __init__(self) -> None:
        pass


if __name__ == '__main__':
    pass
