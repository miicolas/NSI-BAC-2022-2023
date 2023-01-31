def moyenne(lst):
    """Retourne la moyenne pondérée des valeurs de la liste lst."""
    sum_coef = 0 # Somme des coefficients
    sum_val = 0 # Somme des produits des valeurs et des coefficients
    for v, c in lst: # v est la valeur, c est le coefficient
        sum_coef += c # On ajoute le coefficient à la somme des coefficients
        sum_val += v * c # On ajoute le produit de la valeur et du coefficient à la somme des produits
    if sum_coef == 0: # Si la somme des coefficients est nulle, on renvoie None
        return None
    return sum_val / sum_coef # On renvoie la moyenne pondérée


lst = (8, 2), (12, 0), (13.5, 1), (5, 0.5)
print(moyenne(lst))