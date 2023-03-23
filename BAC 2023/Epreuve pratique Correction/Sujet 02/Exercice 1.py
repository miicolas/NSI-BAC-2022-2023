def indices_maxi (tab) : 
    nmax = tab[0]
    for i in range (1,len(tab)): 
        if tab[i]> nmax :
            nmax = tab[i]
    liste_indice = []

    for i in range (len(tab)): 
        if nmax == tab[i]: 
            liste_indice.append(i)
    return (nmax,liste_indice)


print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))