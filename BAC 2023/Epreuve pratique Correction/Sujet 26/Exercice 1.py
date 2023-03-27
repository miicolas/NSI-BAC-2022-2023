def multiplication (n1, n2) : 
    s = 0 
    if n1 == 0 or n2 == 0 : 
        return 0 
    elif n1 < 0 : 
        return -multiplication(-n1, n2)
    elif n2 < 0 : 
        return -multiplication(n1, -n2)
    for i in range(n2) : 
        s = s + n1
    return s 
print(multiplication(-3, -5))