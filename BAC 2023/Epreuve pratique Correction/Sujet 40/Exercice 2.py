class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None
    def getValeur(self):
        return self.valeur
    def droitExiste(self):
        return (self.droit is not None)
    def gaucheExiste(self):
        return (self.gauche is not None)
    def inserer(self, cle):
        if cle < self.valeur :
            if self.gaucheExiste():
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        elif cle > self.valeur:
            if self.droitExiste():
                self.droit.inserer(cle)
            else:
                self.droit  = Noeud(cle)
