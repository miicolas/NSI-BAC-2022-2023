def insere (a,tab):
    """ Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau. """
    l = list(tab)
    l.append(a)
    i = len(l)-2
    while a<l[i] and i>=0:
        # print(l[i])
        l[i+1] = l[i]
        # print(l[i+1])
        l[i] = a
        # print(l[i])
        i = i-1
    return l    
print(insere(8,[1, 2, 3,4,5, 6, 7, 9]))