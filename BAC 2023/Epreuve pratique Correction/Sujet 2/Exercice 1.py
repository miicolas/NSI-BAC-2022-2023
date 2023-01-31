def indices_maxi (tab) : 
    """retourne le maximum et les indices de ses occurrences dans le tableau tab"""
    max_val = max(tab) # On récupère la valeur maximale du tableau
    indice = [] # On crée une liste vide qui contiendra les indices des occurrences du maximum
    if len(tab) == 0 :  # Si la liste est vide, on renvoie False 
        return False
    else : 
        for i in range(len(tab)) :  # On parcourt la liste
            if tab[i] == max_val:   # Si l'élément courant est égal au maximum
                indice.append(i)  # On ajoute l'indice de l'élément courant dans la liste indice
        return (max_val, indice)

tab = 1, 5, 6, 9, 1, 2, 3, 7, 9, 8
print(indices_maxi(tab))
