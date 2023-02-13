class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None


def taille(a):
    """Retourne le nombre de noeuds de l'arbre a"""
    if a == None: # Si l'arbre est vide
        return 0
    return 1+taille(a.fg)+taille(a.fd) # On compte le noeud courant et on ajoute la taille des sous-arbres

def hauteur(a): 
    """Retourne la hauteur de l'arbre a"""
    if a == None:
        return 0
    return 1+max(hauteur(a.fg), hauteur(a.fd)) # On compte le noeud courant et on ajoute la hauteur du plus grand sous-arbre

abr = Arbre(0)
a1 = Arbre(1)
a3 = Arbre(3)
a2 = Arbre(2)
a4 = Arbre(4)
a5 = Arbre(5)
a6 = Arbre(6)

a4.fd = a6
a2.fg = a4
a2.fd = a5
a1.fg = a3
abr.fg = a1
abr.fd = a2