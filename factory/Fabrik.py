__author__ = 'Astrid Krickl'
from factory.Artikel import *
from factory.moreArtikel import *
from factory.diverseFabriken import *


class Fabrik:
    lager = None #artikel array
    @abstractmethod
    def verkaufen(self):
        """
        verkauft aritkel
        """
        pass

    @abstractmethod
    def verpacken(self):
        """
        verpackt artikel
        """
        pass

    @abstractmethod
    def verschicken(self):
        """
        verschickt artikel
        """
        pass

    @classmethod
    def erzeugen(cls, type):
        """
        erzeugt artikel vom angegeben typ
        :param type: artikelart die produziert werden soll
        :return: erzuegter typ
        """

        Fabrik.getFabrik(type).erzeugen(type)
        return type

    @classmethod
    def getFabrik(cls, type):
        """
        gibt die fabrik zurück die verwendet werden soll
        :param type: vom typen artikel der erzeugt werden soll
        :return: fabrik die verwendet werden soll
        """
        if type(type) == Schuhe:
            return Schuhfabrik
        elif type(type) == Computer:
            return Computerfabrik