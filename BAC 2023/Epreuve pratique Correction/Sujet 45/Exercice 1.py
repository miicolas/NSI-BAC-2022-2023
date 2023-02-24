def rangement_valeurs(notes_eval):
    tab = [0]*11 # Création d'un tableau de 11 cases initialisées à 0
    for n in notes_eval: # Pour chaque note de notes_eval
        tab[n] = tab[n] + 1 # On incrémente la case correspondante
    return tab

def notes_triees(effectifs_notes):
    tab = [] # Création d'un tableau vide qui va contenir les notes
    for i in range(len(effectifs_notes)): # Pour chaque case du tableau effectifs_notes (de 0 à 10)
        for _ in range(effectifs_notes[i]): # Pour chaque fois où la note i est présente
            tab.append(i) # On ajoute la note i au tableau tab
    return tab

