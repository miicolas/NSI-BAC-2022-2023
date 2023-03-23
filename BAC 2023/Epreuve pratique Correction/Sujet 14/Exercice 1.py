def recherche (elt, tab) : 
    for i in range (len(tab)): 
        if elt == tab[i] : 
            return i 

    return -1

print(recherche(1, [10, 12, 1, 56]))