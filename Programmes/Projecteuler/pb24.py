def permutations(nb_left:list, pre:str|None=""):
    print(pre, nb_left)
    l_10 = []
    if len(nb_left) > 0:
        for i in nb_left:
            temp_nb_left = nb_left
            temp_nb_left.remove(i)
            l_10.append(permutations(temp_nb_left, str(pre) + str(i)))
    else:
        for i in range(3):
            print(pre, i)
            l_10.append(str(pre)+str(i))
    return l_10

print(permutations([0, 1, 2]))