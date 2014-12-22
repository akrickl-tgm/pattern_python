__author__ = 'Berkay'


# The strategy interface:
class BellVerhalten :
    """
    Das Strategy "Interface" - wird von anderen Klassen geerbt
    """
    # Line is a sequence of points:
    def bellen(self) :
        """
        leere Methode bellen() wird von anderen geerbt und evt. überschrieben
        """
        pass

"""
Beim definieren einer class kann man erben in dem man im Parameter den Namen dieser Klasse angibt.
Wird verwendet für attribut referenzen: Wenn ein benötigtes attribut nicht in dieser Klasse gefunden wird,
wird in der Basis Klasse(welche im Parameter übergeben wurde) gesucht.

Abgeleitete klassen können methoden von der Basis Klasse überschreiben
"""
# Verschiedene Strategys
class LautBellen(BellVerhalten):
    """
    Strategie: Laut bellen
    """
    def bellen(self):
        """
        Bringt den Hund zum Bellen
        """
        return "GANZ LAUT BELLEN!!" # Dummy

class LeiseBellen(BellVerhalten):
    """
    Strategie: Leise bellen
    """
    def bellen(self):
        """
        Bringt den Hund zum Bellen
        """
        return "ganz leise bellen..."  # Dummy

class ElektronischBellen(BellVerhalten):
    """
    Strategie: Elektronisch bellen
    """
    def bellen(self):
        """
        Bringt den Hund zum Bellen
        """
        return "Elekkkkktronisch Bellen!" # Dummy

class AngstBellen(BellVerhalten):
    """
    Strategie: Aus Angst bellen
    """
    def bellen(self):
        """
        Bringt den Hund zum Bellen
        """
        return "bellen aus Angst!" # Dummy

# The "Context" controls the strategy:
class Hund:
    """
    Die Context Klassen zum Kontrollieren der Strategie
    """
    def __init__(self, strategy):
        self.strategy = strategy

    def bellen(self):
        """
        Ruft die bell() Methode je nach Strategie auf
        :return:
        """
        return self.strategy.bellen()

    def changeBellVerhalten(self, newBellVerhalten):
        """
        Verändert das Bell Verhalten
        :param newBellVerhalten:
        :return:
        """
        self.strategy = newBellVerhalten

# Beispiel-Client
meinHund = Hund(LautBellen())
print(meinHund.bellen())

# Die Strategy ändern
meinHund.changeBellVerhalten(LeiseBellen())
print(meinHund.bellen())