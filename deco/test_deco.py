__author__ = 'Astrid Krickl'

from deco.deocrator_himself import *

# diverse decortors
class UpperCase(Decorator):
    txtel = ""

    def __init__(self, txt):
        """
        konstruktor der ein das txtobjekt zu uppercase macht
        :param txt: text der verändert wird
        """
        txtel = self.toString(txt)

    def toString(self, txt):
        """
        funktionalität die das uppercase umssetzt
        :param txt: der text der verndert wird
        :return: der veränderte text
        """
        return txt.upperCase()


class Break(Decorator):
    txtel = ""

    def __init__(self, txt):
        """
        konstruktor der einen zeilenumbruch in den text einfügt
        :param txt: text der verändert wird
        """
        txtel = self.toString(txt)

    def toString(self, txt):
        """
        funktionalität der einen zeilenumbruch an den text anhängt
        :param txt: text der mit einem zeilenumbruch verehen wird
        :return: veränderter text
        """
        return txt + "\n"


class PygLatin(Decorator):
    txtel = ""

    def __init__(self, txt):
        """
        konstruktor der text in pyglatin umwandelt
        :param txt: text der umgewandelt wird
        """
        txtel = self.toString(txt)

    def toString(self, txt):
        """
        Funktionalität die den text in pyglatin übersetzt
        :param txt: text der übersetzt wird
        :return: text der übersetzt wurde
        """
        pyg = 'ay'
        word = txt.lower()
        first = word[0]
        new_word = word+first+pyg
        new_word = new_word[1:len(new_word)]

        if len(txt) > 0 and txt.isalpha():
            return new_word
        else:
            return txt
