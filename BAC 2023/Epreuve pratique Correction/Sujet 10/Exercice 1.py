def maxliste (tab) : 
    maxtab = tab[0]
    for i in range (1, len(tab)): 
        if maxtab < tab[i]: 
            maxtab = tab[i]
    return maxtab

print(maxliste([-27, 24, -3, 15]))