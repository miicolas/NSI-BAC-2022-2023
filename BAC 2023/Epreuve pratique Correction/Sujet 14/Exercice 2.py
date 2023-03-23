def insere(a, tab):
    """ InsÃ¨re l'Ã©lÃ©ment a (int) dans le tableau tab (list)
    triÃ© par ordre croissant Ã  sa place et renvoie le
    nouveau tableau. """
    l = list(tab) #l contient les memes elements que tab
    l.append(a)
    i = len(l)-2
    while a < tab[i] and i >= 0:
        l[i+1] = l[i]
        l[i] = a
        i = i - 1
    return l