def fibonacci (n) : 
    tab = [None]*(n+1)
    tab[1] = 1
    tab[2] = 1
    for i in range(3, n+1):
        tab[i] = tab[i-1] + tab[i-2]
    return tab[n]