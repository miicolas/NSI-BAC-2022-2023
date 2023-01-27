def fusion(tab1, tab2):
    resultat = []
    i, j = 0, 0
    while i < len(tab1) and j < len(tab2):
        if tab1[i] < tab2[j]:
            resultat.append(tab1[i])
            i += 1
        else:
            resultat.append(tab2[j])
            j += 1
    resultat.extend(tab1[i:])
    resultat.extend(tab2[j:])
    return resultat

print(fusion([3, 5], [2, 5]))