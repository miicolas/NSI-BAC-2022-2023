def selection_enclos (tableau_animaux, num_enclos):
    assert type(tableau_animaux) == list
    assert type(num_enclos) == int
    """ Retourne un tableau contenant les animaux de l'enclos num_enclos"""
    result = [] # on crée une liste vide
    for animal in tableau_animaux: # on itère sur les animaux
        if animal['enclos'] == num_enclos: # si l'enclos de l'animal est le bon
            result.append(animal)
    return result

animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
 {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
 {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
 {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
 {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]


assert selection_enclos(animaux, 2) == [{'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2}]
assert selection_enclos(animaux, 5) == [{'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5}, {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]
assert selection_enclos(animaux, 7) == []

