def recherche (a, tab): 
    r = 0
    for i in range (len(tab)) : 
        if a == tab[i] : 
            r+= 1
    return r 

print(recherche(5, [-2, 5, 3, 5, 4, 5]))

