def recherche_min (tab) : 
    minim = tab[0]
    indice_min = 0
    for i in range (1,len(tab)):
        if minim > tab[i] : 
            indice_min = i
            minim = tab[i]

    return indice_min

print(recherche_min([5]))
print(recherche_min([2,4,1]))
print(recherche_min([5,3,2,2,4]))