def recherche (elt,tab): 
    """renvoie l'indice de la première occurrence de elt dans tab ou -1 si elt n'est pas dans tab"""
    nombre_valeur = len(tab) # On récupère la longueur du tableau
    for i in range(nombre_valeur): # On parcourt le tableau
        if elt == tab[i]: # Si l'élément courant est égal à elt
            return i  
    return -1

print(recherche(5,[9, 0, 8, 5, 0, 2, 7, 1, 5, 3, 6]))
