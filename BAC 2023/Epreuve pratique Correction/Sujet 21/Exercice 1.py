def delta(liste) :
    """Renvoie la liste des différences successives entre les éléments de la liste liste."""
    val_debut = liste[0]  # On récupère la première valeur de la liste
    for i in range(len(liste)-1) :  # On parcourt la liste 
        liste[i] = liste[i+1] - liste[i]  # On remplace l'élément courant par la différence entre l'élément suivant et l'élément courant
    liste.pop()  # On supprime le dernier élément de la liste
    liste.insert(0,val_debut)  # On insère la première valeur de la liste au début de la liste (on l'a supprimée précédemment)
    return liste

print(delta([1000, 800, 802, 1000, 1003])
)

