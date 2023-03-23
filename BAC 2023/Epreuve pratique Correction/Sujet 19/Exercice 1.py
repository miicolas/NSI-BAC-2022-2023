def recherche (tab, n):
    debut = 0 
    fin = len (tab) - 1
    indice = -1 
    while debut <= fin and indice == -1 : 
        milieu = (debut+fin)//2
        if tab[milieu] == n :
            indice = tab[milieu]
        elif tab[milieu] > n : 
            fin = milieu -1 
        else : 
            debut = milieu + 1

    return indice



print(recherche([2, 3, 4, 5, 6], 5))
