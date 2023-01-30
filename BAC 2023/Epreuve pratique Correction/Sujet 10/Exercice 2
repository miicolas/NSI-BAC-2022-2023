class Pile:
    """
    Classe definissant une pile
    """
    def __init__(self):
        self.valeurs = []

    def est_vide(self):
        """
        Renvoie le booleen True si la pile est vide, False sinon.
        """
        return self.valeurs == []
    
    def empiler(self, v):
        """
        Place l'element v au sommet de la pile
        """
        self.valeurs.append(v)

    def depiler(self):
        """
        Retire et renvoie l'element place au sommet de la pile,
        si la pile n'est pas vide.
        """
        if not self.est_vide():
            return self.valeurs.pop()
    
    def parenthesage(ch):
        """
        Renvoie True si la chaine ch est bien parenthesee et False sinon
        """
        p = Pile()
        for c in ch:
            if c == '(':
                p.empiler(c)
            elif c == ')':
                if p.est_vide():
                    return False
                p.depiler()
        return p.est_vide()