def maxliste (tab) :
    """renvoie le maximum d'un tableau non vide tab"""
    maximum = tab[0] # On initialise le maximum à la première valeur du tableau
    for i in range(len(tab)):  # On parcourt le tableau
        if maximum < tab[i] :  # Si le maximum est plus petit que l'élément courant
            maximum = tab[i] # On met à jour le maximum
    return maximum
    
tab = -27, 24, -3, 15

print(maxliste(tab))
        



