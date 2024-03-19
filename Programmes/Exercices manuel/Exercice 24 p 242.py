def get_pairs(sandwiches:list[tuple[str, float|int]], boissons:list[tuple[str, float|int]]):
    """Returns minimized calories pairs from two lists of tuples containing name/calories pairs"""


    # On vérifie que l'argument sandwiches est du bon type

    if not isinstance(sandwich, (list, tuple)):
        raise TypeError("argument sandwiches must be a list or a tuple")
    else:
        for sandwich in sandwiches:
            if not isinstance(sandwich, (list, tuple)):
                raise TypeError("sandwiches must be a list or a tuple containing name, calories in this order")
            else:
                if not isinstance(sandwich[0], str):
                    raise TypeError("name of sandwich must be a string")
                if not isinstance(sandwich[1], (int, float)):
                    raise TypeError("calories of sandwich must be an int or a float")
                if len(sandwich) != 2 :
                    raise ValueError("Sandwiches airs must only contain 2 values")

    # On vérifie que l'argument boissons est du bon type

    if not isinstance(boissons, (list, tuple)):
        raise TypeError("argument boissons must be a list or a tuple")
    else:
        for boisson in boissons:
            if not isinstance(boisson, (list, tuple)):
                raise TypeError("boisson must be a list or a tuple containing name, calories in this order")
            else:
                if not isinstance(boisson[0], str):
                    raise TypeError("name of boisson must be a string")
                if not isinstance(boisson[1], (int, float)):
                    raise TypeError("calories of boisson must be an int or a float")
                if len(boisson) != 2 :
                    raise ValueError("Boissons pairs must only contain 2 values")
                
    # On vérifie que les 2 listes ont la même longueur
                
    if len(sandwiches) != len(boissons):
        raise ValueError("Both arguments must have the same length")

    # On trie les listes; une dans l'ordre croissant, l'autre dans l'ordre décroissant

    sand_sorted = sorted(sandwiches, key=lambda calories: calories[1])
    boissons_sorted = sorted(boissons, key=lambda calories: calories[1], reverse=True)

    pairs = []

    # Pour chaque élément d'une liste, on lui associe l'élément inverse de l'autre (et aussi la valeur des calories totales)

    for index, sandwich in enumerate(sand_sorted):
        pairs.append((sandwich[0], boissons_sorted[index][0], str(sandwich[1] + boissons_sorted[index][1])))

    return pairs

if __name__ == "__main__":
    sandwiches = [
        ("Jambon beurre", 100),
        ("beurre", 20),
        ("Jambon", 80),
    ]

    boissons = [
        ("coca", 150),
        ("ice tea", 80),
        ("Eau", 0),
    ]

    print(get_pairs(sandwiches, boissons))