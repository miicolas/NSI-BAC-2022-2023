def taille (arbre, lettre): 
    if lettre == " " : 
        return 0
    return 1+ taille(arbre, arbre[lettre][1]) + taille(arbre[lettre][0])

