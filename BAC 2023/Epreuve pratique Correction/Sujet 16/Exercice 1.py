def recherche_indices_classement (elt, tab) : 
    tab_min = []
    tab_moy = []
    tab_max = []
    for i in range(len(tab)): 
        if tab[i] == elt : 
            tab_moy.append(i)
        elif tab[i] > elt : 
            tab_max.append(i)
        else: 
            tab_min.append(i)
    
    return tab_min, tab_moy, tab_max

print(recherche_indices_classement(3, []))