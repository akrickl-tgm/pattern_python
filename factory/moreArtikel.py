__author__ = 'Astrid Krickl'
from factory.Artikel import *


class Schuhe(Artikel):

    groesse = 38

    def anziehen(self):
        """
        methode zum schuhe anziheen
        """
        pass

    def getprise(self):
        """
        methode vom quasi interface Artikel implementiert
        :return: preis von dem schuh
        """
        return 10


class Computer(Artikel):
    benchmark = ""

    def aufdrehen(self):
        """
        methode zum aufdrehen des computers
        :return:
        """
        pass

    def getprise(self):
        """
        implementierung vom quasi interface artikel
        :return: preis vom computer
        """
        return 300