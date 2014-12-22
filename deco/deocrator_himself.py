__author__ = 'Astrid Krickl'
from deco.TextElement import *


class Decorator(TextElement):
    # erbt von Textelement
    txtEl = TextElement()

    @abstractmethod
    def toString(self):
        """
        Methode die jeder Decorator haben muss als vorrausetzung
        :return: veränderter text
        """
        pass
