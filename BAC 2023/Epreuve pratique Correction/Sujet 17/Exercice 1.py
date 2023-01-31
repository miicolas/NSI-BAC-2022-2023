def moyenne (liste_notes) :
    assert type(liste_notes) == list
    """Renvoie la moyenne pondérée des notes de la liste liste_notes."""
    somme = 0
    coefficients = 0
    for note,coefficient in liste_notes : # On parcourt la liste
        somme += note * coefficient # On ajoute le produit de la note et du coefficient à la somme
        coefficients += coefficient # On ajoute le coefficient à la somme des coefficients
    return somme / coefficients # On renvoie la moyenne pondérée

assert moyenne([(15, 2), (9, 1), (12, 3)]) == 12.5

