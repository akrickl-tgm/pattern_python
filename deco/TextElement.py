__author__ = 'Astrid Krickl'
from deco.test_deco import *


class TextElement:
    """
    stellt das TextElement da
    """
    @abstractmethod
    def toString(self):
        pass


class TextElementText(TextElement):
    """
    Klasse die das TextElement verwendet
    """
    txt = ""

    def __init__(self, txt):
        self.txt = txt

    def toString(self):
        pass


#verwenden von decorators
meintext = TextElementText("haallo")
print('%s' % (PygLatin(UpperCase(meintext))))

print('%s' % (Break(UpperCase("servus"))))

