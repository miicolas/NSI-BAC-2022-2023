def recherche_min (tab): 
    min_value = 0
    for i in range(len(tab)-1): 
        if tab[i] > tab[i+1] : 
            min_value = i+1
        else : 
            pass
    return min_value

assert recherche_min([5]) == 0
assert recherche_min([2, 4, 1]) == 2
assert recherche_min([5, 3, 2, 2, 4]) == 2