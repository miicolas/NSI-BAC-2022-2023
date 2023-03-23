dico = {'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}

def max_dico (dico) : 
    val_max = 0
    nom_max = 0
    for nom in dico :
        if dico[nom] > val_max : 
            val_max = dico[nom] 
            nom_max = nom
    return val_max, nom_max

print(max_dico(dico))