def recherche (elt , tab) : 
    for i in reversed (range (len(tab))) : #
        if tab[i] == elt : 
            return i

print(recherche(1, [8,1,10,1,7,1,8]))
