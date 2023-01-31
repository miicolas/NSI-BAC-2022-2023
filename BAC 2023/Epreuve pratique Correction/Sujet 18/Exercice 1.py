def max_et_indice (tab): 
    """retourne le maximum et son indice dans le tableau tab"""
    t = len(tab)
    max_val = tab[0] # On initialise le maximum à la première valeur du tableau
    max_ind = 0 # On initialise l'indice du maximum à 0
    for i in range(1,t): # On parcourt le tableau à partir de l'indice 1
        if tab[i] > max_val: # Si l'élément courant est plus grand que le maximum
            max_val = tab[i] # On met à jour le maximum
            max_ind = i # On met à jour l'indice du maximum
    return (max_val, max_ind) 
print(max_et_indice([1, 5, 6, 0, 9, 2, 3, 7, 9, 10])
)
