def moyenne (tab) : 
    somme = 0
    for i in range (len(tab)) : 
        somme += tab[i]
    return somme / len(tab)

