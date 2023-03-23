def ajoute_dictionnaires (d1,d2): 

    d = {}
    for i in d1 : 
        if i in d2: 
            d[i] = d1[i] + d2[i]
        else : 
            d[i] = d1[i]

    for i in d2 : 
        if i not in d : 
            d[i] = d2[i]

    return d