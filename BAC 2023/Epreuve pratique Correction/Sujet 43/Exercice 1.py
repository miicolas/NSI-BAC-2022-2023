def ecriture_binaire_entier_positif (n):
    'Ecriture binaire d un entier positif'
    r = []
    if n == 0:
        return "0"
    else:
        while n != 0:
            r.append(n % 2)
            n = n // 2
        r.reverse()
        return r
        
n = 105
print(ecriture_binaire_entier_positif(n))