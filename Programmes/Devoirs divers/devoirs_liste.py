def occurence(tab:list, element)->int:
    '''Retourne le nombre d'occurences de l'élément dans la liste'''
    occs = 0
    for i in tab:
        if element == i:
            occs += 1
    return occs

def occurences_uniques(tab:list)->list:
    nb = 0
    elts = []
    tab.sort()
    for i, element in enumerate(tab):
        if i < len(tab)-1:
            if element != tab[i-1] and element != tab[i+1]:
                nb += 1
                elts.append(element)
    if element != tab[len(tab)-2]:
        nb += 1
        elts.append(element) 
    return nb, elts

def anagramme(mot1:str, mot2:str)->bool:
    '''Retourne True si les 2 mots sont anagrammes, sinon retourne False'''
    list1 = [ord(char) for char in mot1]
    list2 = [ord(char) for char in mot2]
    list1.sort()
    list2.sort()
    return list1 == list2

def elt_max(tab:list):
    '''Retourne l'élément le plus présent dans une liste'''
    occs_max = 0
    for char in tab:
        if occurence(tab, char) > occs_max:
            char_max = char
            occs_max = occurence(tab, char)
    return occs_max, char_max

print(occurences_uniques([1, 2, 3, 2, 4, 4, 3, 1, 5, 3, 8, 8, 7, 9, 8]))