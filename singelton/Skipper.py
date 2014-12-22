__author__ = 'Astrid Krickl'
from singelton.Schiffsboerse import *


class Skipper:
    anzahlSchiffe = 0

    def __init__(self, anzSchiffe):
        """
        konstruktor der einen neuen skipper anlegt und eröffnet eine börse
        :param anzSchiffe: schiffe die der skipper schon besitzt
        """
        self.anzahlSchiffe = anzSchiffe
        Schiffsboerse() #eröffnen der Börse

    def verkaufeSchiffbeiBoerse(self):
        """
        verkauft ein schiff vom skipper an die boerse
        """
        self.anzahlSchiffe -= 1
        Schiffsboerse.getInstance().kaufeSchiff()

    def kaufeSchiffbeiBoerse(self):
        """
        Kauft ein schiff von der boerse
        """
        self.anzahlSchiffe += 1
        Schiffsboerse.getInstance().verkaufeSchiff()

    def getLagerbestand(self):
        """
        gibt den lagerbestand des skippers zurück
        :return: aktueller lagerbestand
        """
        return self.anzahlSchiffe

skipper1 = Skipper(3)
skipper2 = Skipper(5)

print("%d" % (Schiffsboerse.getInstance().getLagerbestand()))
skipper1.kaufeSchiffbeiBoerse()
print("%d" % (Schiffsboerse.getInstance().getLagerbestand()))
skipper2.verkaufeSchiffbeiBoerse()
skipper1.verkaufeSchiffbeiBoerse()
print("%d" % (Schiffsboerse.getInstance().getLagerbestand()))

