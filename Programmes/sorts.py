def insersion_sort(inp)->list:
    to_sort = inp
    if not isinstance(to_sort, list):
        raise TypeError
    if len(to_sort) == 0:
        raise Exception("Length of the list must not be 0", to_sort)
    sorted = []
    while len(to_sort)>0:
        val = to_sort[0]
        for i in to_sort:
            if i < val:
                val = i
        sorted.append(val)
        to_sort.remove(val)
    return sorted