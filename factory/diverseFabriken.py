__author__ = 'Astrid Krickl'
from factory.Fabrik import *


class Computerfabrik(Fabrik):
    computer = None #compzter array

    def verkaufen(self):
        """
        verkauft computer
        :return:
        """
        pass

    def verpacken(self):
        """
        verpackt computer
        :return:
        """
        pass

    def verschicken(self):
        """
        verschickt computer
        :return:
        """
        pass


class Schuhfabrik(Fabrik):
    schuhe = None #schuhe array

    def verkaufen(self):
        """
        verkauft schuhe
        :return:
        """
        pass

    def verpacken(self):
        """
        verpackt schuhe
        :return:
        """
        pass

    def verschicken(self):
        """
        verschickt schuhe
        :return:
        """
        pass

