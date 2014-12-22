__author__ = 'Astrid Krickl'
from factory.Artikel import *
from factory.moreArtikel import *
from factory.diverseFabriken import *


class Fabrik:
    lager = None #artikel array
    @abstractmethod
    def verkaufen(self):
        pass

    @abstractmethod
    def verpacken(self):
        pass

    @abstractmethod
    def verschicken(self):
        pass

    @classmethod
    def erzeugen(cls, type):
        if type(type) == Schuhe:
            return Schuhe
        elif type(type) == Computer:
            return Computer

    @classmethod
    def getFabrik(cls, type):
        if type(type) == Schuhfabrik:
            return Schuhfabrik
        elif type(type) == Computerfabrik:
            return Computerfabrik