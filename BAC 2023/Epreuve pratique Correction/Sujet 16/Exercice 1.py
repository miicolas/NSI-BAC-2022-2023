def recherche_indices_classement(elt,tab):
    """renvoie les indices des éléments de tab inférieurs, égaux et supérieurs à elt""" 
    t= len(tab) # On récupère la longueur du tableau
    l = [] # On crée une liste vide qui contiendra les indices des occurrences de elt
    l1 = [] # On crée une liste vide qui contiendra les indices des occurrences des éléments inférieurs à elt
    l2 = [] # On crée une liste vide qui contiendra les indices des occurrences des éléments supérieurs à elt
    for i in range(t): # On parcourt le tableau
        if elt == tab[i]: # Si l'élément courant est égal à elt
            l.append(i) # On ajoute l'indice de l'élément courant dans la liste l
            
    for i in range(t): # On parcourt le tableau
        if elt > tab[i]: # Si l'élément courant est inférieur à elt
            l1.append(i) # On ajoute l'indice de l'élément courant dans la liste l1
            
    for i in range(t): # On parcourt le tableau
        if elt < tab[i]: # Si l'élément courant est supérieur à elt
            l2.append(i) # On ajoute l'indice de l'élément courant dans la liste l2

    return l1,l,l2
            

print(recherche_indices_classement(5,[9, 0, 8, 5, 0, 2, 7, 1, 5, 3, 6]))