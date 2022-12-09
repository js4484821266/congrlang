import re
import cngr as C
def eval(word:str):#->int:
    w=re.sub('[^'+''.join(C.V+C.C)+']*','',word)
    
if __name__=='__main__':
    print(eval('cdsfcsdfscf22222cdfqqq'))