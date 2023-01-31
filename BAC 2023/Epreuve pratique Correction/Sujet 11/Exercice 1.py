def convertir (tab):
    """renvoie le nombre décimal correspondant au nombre binaire contenu dans le tableau tab""" 
    nombre = 0
    for i in range (len(tab)): # On parcourt le tableau
        nombre = tab[i]*(2**(len(tab) - i - 1)) + nombre # On ajoute le produit de l'élément courant par 2 puissance la longueur du tableau moins l'indice courant moins 1
    return nombre

    
tab = 1, 0, 1, 0, 0, 1, 1
print(convertir(tab))