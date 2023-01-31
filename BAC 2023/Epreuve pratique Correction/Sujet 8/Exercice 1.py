def max_dico(dico):
    max_value = max(dico.values())
    max_key = [k for k, v in dico.items() if v == max_value][0]
    return (max_key, max_value)



dico = {'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}
print(max_dico(dico))