def inverse_chaine(chaine): 
    result = ""
    for caractere in chaine:
        result = caractere + result
    return result

def est_palindrome(chaine): 
    inverse = inverse_chaine(chaine)
    return chaine == inverse

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)


print(inverse_chaine("bonjour"))
print(est_palindrome("bonjour"))
print(est_nbre_palindrome(12321))