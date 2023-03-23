def nbr_occurence (chaine): 
    d = {}
    for i in chaine: 
        if i in d  :
            d[i] += 1
        else : 
            d[i] = 1

    return d 

print(nbr_occurence('Hello'))