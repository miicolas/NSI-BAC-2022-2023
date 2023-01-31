def multiplication (n1,n2) :
    """ fonction qui multiplie deux nombres entiers positifs ou négatifs"""
    r = 0
    if n2 > 0 : # si n2 est positif
        for k in range (n2) :  # on fait n2 additions
            r = n1 + r # on ajoute n1 à r
        return r
    elif n2 < 0 and n1 < 0 :   # si n2 et n1 sont négatifs
        n2 = abs(n2) # on les rend positifs
        n1 = abs(n1)  
        for k in range (n2) :  # on fait n2 additions
            r = n1 + r # on ajoute n1 à r
        return r



print(multiplication(-4,-8))