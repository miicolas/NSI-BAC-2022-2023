def nbr_occurences (chaine): 
    d = {}
    for letter in chaine : 
        if letter in d : 
            d[letter] += 1
        else  : 
            d[letter] = 1
    return d 

print(nbr_occurences('bonjour'))
