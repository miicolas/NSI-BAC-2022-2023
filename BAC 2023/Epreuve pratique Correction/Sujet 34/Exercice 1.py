def moyenne (tab) : 
    somme = 0
    n = len(tab)
    for i in range (len(tab)): 
        somme += tab[i]

    return somme / n

print(moyenne([5, 3, 8])
)
print(moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
)