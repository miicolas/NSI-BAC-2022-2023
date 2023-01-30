def rendu_monnaie(somme_due, somme_versee): 
    rendu = []
    a_rendu =somme_versee - somme_due
    i = len(pieces)-1
    while i >= 0:
        if a_rendu >= pieces[i]: 
            rendu.append(pieces[i])
            a_rendu = a_rendu - pieces[i]
        else:
            i = i - 1
    return rendu

pieces = [1, 2, 5, 10, 20, 50, 100, 200]
print(rendu_monnaie(10, 100))
