def multiplication (n1, n2) :
    r = 0
    
    if n1>0 and n2>0 : 
        for i in range (n1) :
            r += n2
    elif n1<0 and n2>0 :
        for i in range(n2) : 
            r += n1
    elif n1>0 and n2<0 :
        for i in range(n1) : 
            r += n2
    else : 
        n1 = abs(n1)
        n2 = abs(n2)
        for i in range (n1): 
            r += n2

    return r

print(multiplication(-3, -5))