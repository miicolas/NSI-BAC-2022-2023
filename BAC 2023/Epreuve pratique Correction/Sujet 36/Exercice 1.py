def couples_consecutifs (L):
    """renvoie la liste des couples consécutifs de L
    exemple : couples_consecutifs([1,2,3,4,5]) renvoie [(1,2),(2,3),(3,4),(4,5)]"""
    r = []
    for i in range(len(L)-1):
        if L[i+1] -  L[i] == 1:
            r.append((L[i],L[i+1]))
    return r
            

print(couples_consecutifs([1,4,3,5]))
