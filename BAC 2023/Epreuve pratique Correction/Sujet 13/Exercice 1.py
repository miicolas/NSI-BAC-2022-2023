def recherche (a, tab) :
    """renvoie le nombre d'occurrences de a dans tab"""
    r = 0 
    for i in range(len(tab)): # On parcourt le tableau
        if tab[i]== a : # Si l'élément courant est égal à a
            r+= 1 # On incrémente r de 1
    return r

assert recherche (5, [-2, 5, 3, 5, 4, 5]) ==3