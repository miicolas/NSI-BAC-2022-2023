def recherche_indices_classement(elt,tab): 
    t= len(tab)
    l = []
    l1 = []
    l2 = []
    for i in range(t):
        if elt == tab[i]:
            l.append(i)
            
    for i in range(t):
        if elt > tab[i]:
            l1.append(i)
            
    for i in range(t):
        if elt < tab[i]:
            l2.append(i)

    return l1,l,l2
            

print(recherche_indices_classement(5,[9, 0, 8, 5, 0, 2, 7, 1, 5, 3, 6]))