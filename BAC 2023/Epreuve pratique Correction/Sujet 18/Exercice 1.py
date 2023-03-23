def max_et_indice(tab) : 
    max_indice = 0 
    max_value = tab[0]
    for i in range (1, len(tab)) : 
        if max_value < tab[i] : 
            max_value = tab[i]
            max_indice = i

    return max_value,max_indice

print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))