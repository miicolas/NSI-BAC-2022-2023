def recherche (tab, n):
    """recherche dichotomique du nombre entier n dans le tableau non vide tab trié par ordre croissant"""
    for i in reversed(range(len(tab))) :  # On parcourt la liste à l'envers
        if tab[i] == n :  # Si l'élément courant est égal à n
            return i 
        return len(tab) # Si n n'est pas dans la liste, on renvoie la longueur de la liste

print(recherche([5, 3], 1))