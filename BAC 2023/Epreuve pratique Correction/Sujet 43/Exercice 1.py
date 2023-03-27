def ecriture_binaire_eniter_positif (n) : 
    liste = [n%2]
    n = n//2
    while n >0 : 
        liste.append(n%2)
        n = n//2
    liste.reverse()
    return liste
    
