def fusion(tab1, tab2):
    """Retourne la fusion de deux tableaux triés en ordre croissant."""
    resultat = [] # Le tableau résultat
    i, j = 0, 0 # i et j sont les indices des éléments courants dans tab1 et tab2
    while i < len(tab1) and j < len(tab2): # Tant qu'on n'a pas parcouru tous les éléments de tab1 et tab2
        if tab1[i] < tab2[j]: # Si l'élément courant de tab1 est plus petit que celui de tab2
            resultat.append(tab1[i]) # On ajoute l'élément courant de tab1 dans le tableau résultat
            i += 1 # On passe à l'élément suivant de tab1
        else:
            resultat.append(tab2[j]) # On ajoute l'élément courant de tab2 dans le tableau résultat
            j += 1 # On passe à l'élément suivant de tab2
    resultat.extend(tab1[i:]) # On ajoute les éléments restants de tab1 dans le tableau résultat
    resultat.extend(tab2[j:]) 
    return resultat

print(fusion([3, 5], [2, 5]))

