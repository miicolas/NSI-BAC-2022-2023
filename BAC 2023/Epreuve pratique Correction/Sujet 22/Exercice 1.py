def liste_puissances (a, n) : 
    L = []
    b = 1
    for i in range (n) : 
        b = a * b
        L.append(b)
    return L

def liste_puissances_borne (a, borne): 
    L=[]
    b= 1
    while b < borne  : 
        b = a*b
        L.append(b)
    L.pop()
    return L


print(liste_puissances(-2,4))
print(liste_puissances_borne(5,5))