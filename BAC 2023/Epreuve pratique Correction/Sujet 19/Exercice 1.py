def recherche (tab, n):
    """recherche dichotomique du nombre entier n dans le tableau non vide tab trié par ordre croissant"""
    assert len(tab) > 0 # On vérifie que le tableau n'est pas vide
    assert tab == sorted(tab) # On vérifie que le tableau est trié
    i = 0 
    j = len(tab) - 1   # On initialise les indices de début et de fin
    while i<=j :  # Tant que l'indice de début est inférieur ou égal à l'indice de fin
        m = (i+j)//2 # On calcule l'indice du milieu
        if tab[m] == n :  # Si l'élément du milieu est égal à n
            return m 
        elif tab[m] > n : # Si l'élément du milieu est supérieur à n
            j = m - 1 # On décale l'indice de fin
        else: 
            i = m + 1 # On décale l'indice de début
    return -1


assert recherche([2, 3, 4, 5, 6], 5) == 3
assert recherche([2, 3, 4, 6, 7], 5) == -1




















