__author__ = 'Astrid Krickl'

class Artikel:
    #so quasi interface
    @abstractmethod
    def getprise(self):
        """
        gibt den preis eines artikels an
        :return: artikelpreis
        """
        pass
