def tri_selection (tab): 
    for i in range(len(tab)-1) : 
        min_i = i 
        for j in range(i+1, len(tab)): 
            if tab[j] < tab[min_i] : 
                min_i = j
        tab[i], tab[min_i] = tab[min_i], tab[i]

    return tab