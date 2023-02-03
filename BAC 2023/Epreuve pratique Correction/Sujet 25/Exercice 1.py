def enumere (L): 
    """Écrire une fonction enumere qui prend en paramètre une liste L et renvoie un
    dictionnaire d dont les clés sont les éléments de L avec pour valeur associée la liste des
    indices de l’élément dans la liste L"""
    d = {} # on crée un dictionnaire vide
    for i in range(len(L)):
        if L[i] in d:
            d[L[i]].append(i)
        else:
            d[L[i]] = [i]
    return d

print(enumere([1, 1, 2, 3, 2, 1]))
        