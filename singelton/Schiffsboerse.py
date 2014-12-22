__author__ = 'Astrid Krickl'


class Schiffsboerse:
    lagerbestand = 30
    instance = None

    def __init__(self):
        """
        legt eine neue schiffsboerse an falls noch keine vorhanden ist, ansonsten passiert nichts
        """
        if self.instance is None:
            self.instance = Schiffsboerse

    @classmethod
    def getInstance(self):
        """
        Statische Methode die die instanz der Klasse zurückgibt, diese wird aber nur einmal angelegt udn sonst immer
        die selbe zurückgegeben
        :return: instanz der Klasse
        """
        if self.instance is None:
            self.instance = Schiffsboerse
        else:
            return self.instance

    def verkaufeSchiff(self):
        """
        verkauft ein schiff
        :return: ob der verkauf erfolgreich war
        """
        self.lagerbestand -= 1
        return True

    def kaufeSchiff(self):
        """
        kauft ein Schiff
        """
        self.lagerbestand += 1

    def getLagerbestand(self):
        """
        zeigt wie voll das lager ist
        :return: aktueller lagerbestand
        """
        return self.lagerbestand