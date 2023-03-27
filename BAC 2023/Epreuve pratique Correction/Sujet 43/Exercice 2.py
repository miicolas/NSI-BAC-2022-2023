def tri_bulles(T):
    '''
	Renvoie le tableau T triÃƒÂ© par ordre croissant
	'''
    n = len(T)
    for i in range(len(T),0,-1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T