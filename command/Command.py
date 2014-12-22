__author__ = 'Berkay'
"""
Mit dem Command-Design Pattern kann man bestimmte Aktionen einer Methode oder einem Objekt übergeben
=> Ein Befehl als Objekt kapseln:

Dies ermöglicht es, Klienten mit verschiedenen Anfragen zu parametrisieren,
Operationen in eine Schlange zu stellen, ein Logbuch zu führen und Operationen rückgängig zu machen.

"""
# Sozuasgen das Interface
class DruckBefehl:
    """
    Dient sozusagen als "Interface", wird von anderen abgeleitet
    """
    def drucken(self):
        pass

# konkrete Durchführung
class SchwarzWeissDruck(DruckBefehl):
    """
    SchwarzWeiß - Drucker
    """
    def drucken(self):
        """
        druckt Schwarz/Weiss aus
        :return: _string
        """
        print("==== Schwarz/Weiß gedruckt ====")

# konkrete Durchführung
class FarbDruck(DruckBefehl):
    """
    FarbDruck - Drucker
    """
    def drucken(self):
        """
        druckt FARBIG aus
        :return _string:
        """
        print("==== FARBIG gedruckt ====")

# konkrete Durchführung
class PDFDruck(DruckBefehl):
    """
    PDFDruck - Drucker
    """
    def drucken(self):
        """
        druckt PDF aus - Ausgabe durch print(..)
        """
        print("==== PDF - Druck ====")


# An object that holds commands:
class Drucker:
    """
    Drucker das die Commandos hält
    """
    def __init__(self):
        """
        Beim Aufruf dieser Klasse
        :rtype : object
        :return: None
        """
        self.druckAuftraege = []  # leeres Array

    def addAuftrag(self, druckAuftrag):
        """
        Fügt ein Druckauftrag zur Auftragsliste hinzu
        :param druckAuftrag:
        :return: None
        """
        self.druckAuftraege.append(druckAuftrag) # dem Array hinzufügen

    def run(self):
        """
        Durchführung aller Druckaufträge
        :return:
        """
        for c in self.druckAuftraege:
            c.drucken()

# Beispiel - Client
meinDrucker = Drucker()
meinDrucker.addAuftrag(SchwarzWeissDruck())
meinDrucker.addAuftrag(FarbDruck())
meinDrucker.addAuftrag(PDFDruck())
meinDrucker.run()