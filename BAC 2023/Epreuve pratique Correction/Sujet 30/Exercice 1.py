def moyenne (tab) : 
    """"renvoie la moyenne des éléments de tab"""
    s = 0
    if len(tab) == 0: # Si le tableau est vide
        return 0
    if len(tab) == 1: # Si le tableau contient un seul élément
        return tab[0]
    for i in range(len(tab)): # On parcourt le tableau
        s+= tab[i] # On ajoute l'élément courant à la somme
    return s/len(tab) # On renvoie la moyenne

assert moyenne ([1.0, 2.0, 4.0]) == 2.3333333333333335
assert moyenne ([1.0]) == 1.0