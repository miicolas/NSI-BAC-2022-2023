liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j sert à déterminer où placer la valeur à ranger
        j = i - 1
        # tant qu'on a pas trouvé la place de l'élément à insérer
        # on décale les valeurs du tableau vers la droite
        while j >= 0 and valeur_insertion < tab[j]:
            tab[j + 1] = tab[j]
            j = j - 1
        tab[j] = valeur_insertion
        return tab

print(tri_insertion(liste))