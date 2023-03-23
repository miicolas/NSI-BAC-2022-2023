def recherche (tab, n) : 
    for i in reversed(range(len(tab))): 
        if tab[i] == n : 
            return i

    return len(tab)
print(recherche([2, 3, 5, 2, 4], 2))