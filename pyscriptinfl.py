from pyscript import Element
from infl import infl


def inflinfl():
    aaaa = int(Element('aaaa').element.value)
    bbbb = int(Element('bbbb').element.value)
    Element('apbn').write(infl(aaaa, bbbb, 2147483647))
