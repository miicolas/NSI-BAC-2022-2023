def multiplication (n1,n2) :
    r = 0  
    if n1 > 0 and n2 > 0: 
        for k in range (n2) :
            r += n1

    if n1 < 0 and n2 < 0:
        n1 = abs(n1)
        n2 = abs(n2)
        for k in range (n2) :
            r += n1

    if n1 < 0 and n2 > 0:
        n1 = abs(n1)
        for k in range (n2) :
            r -= n1

    if n1 > 0 and n2 < 0:
        n2 = abs(n2)
        for k in range (n2) :
            r -= n1 


    return r

print(multiplication(-4,8)) 
