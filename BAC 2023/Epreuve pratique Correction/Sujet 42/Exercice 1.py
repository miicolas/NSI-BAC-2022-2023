def tri_selection (tab) : 
    """renvoie le tableau tab trié par ordre croissant"""
    for i in range (len(tab)-1) :
        min = i
        for j in range (i+1, len(tab)) :
            if tab[j] < tab[min] :
                min = j
        tab[i], tab[min] = tab[min], tab[i]
    return tab


tab = [1,52,6,-9,12]

print(tri_selection(tab))
        
