__author__ = 'SECKIN Berkay'


# The strategy interface:
class BellVerhalten :
    # Line is a sequence of points:
    def bellen(self) : pass

"""
Beim definieren einer class kann man erben in dem man im Parameter den Namen dieser Klasse angibt.
Wird verwendet für attribut referenzen: Wenn ein benötigtes attribut nicht in dieser Klasse gefunden wird,
wird in der Basis Klasse(welche im Parameter übergeben wurde) gesucht.

Abgeleitete klassen können methoden von der Basis Klasse überschreiben
"""
# Verschiedene Strategys
class LautBellen(BellVerhalten):
    def bellen(self):
        return "GANZ LAUT BELLEN!!" # Dummy

class LeiseBellen(BellVerhalten):
    def bellen(self):
        return "ganz leise bellen..."  # Dummy

class ElektronischBellen(BellVerhalten):
    def bellen(self):
        return "Elekkkkktronisch Bellen!" # Dummy

class AngstBellen(BellVerhalten):
    def bellen(self):
        return "bellen aus Angst!" # Dummy

# The "Context" controls the strategy:
class Hund:
    def __init__(self, strategy):
        self.strategy = strategy

    def bellen(self):
        return self.strategy.bellen()

    def changeBellVerhalten(self, newBellVerhalten):
        self.strategy = newBellVerhalten

# Beispiel-Client
meinHund = Hund(LautBellen())
print(meinHund.bellen())

# Die Strategy ändern
meinHund.changeBellVerhalten(LeiseBellen())
print(meinHund.bellen())