def multiplication (n1,n2) :
    r = 0
    if n2 > 0 :
        for k in range (n2) : 
            r = n1 + r
        return r
    elif n2 < 0 and n1 < 0 :  
        n2 = abs(n2)
        n1 = abs(n1)
        for k in range (n2) : 
            r = n1 + r
        return r



print(multiplication(-4,-8))