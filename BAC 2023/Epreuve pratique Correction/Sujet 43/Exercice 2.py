def tri_bulles(T):
    '''
	Renvoie le tableau T triÃƒÂ© par ordre croissant
	'''
    n = len(T)
    for i in range(n-1,0,-1): # On parcourt le tableau de la fin vers le début
        for j in range(i):
            if T[j] > T[i]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp 
    return T