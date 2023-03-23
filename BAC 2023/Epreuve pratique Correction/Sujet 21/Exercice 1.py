def delta (liste): 
    tab = (liste[0])
    for i in range (1, len(liste)): 
        tab.append(liste[i]- liste[i-1])

    return tab