t = ['aa', 'aa', 'b', 'c', 'c', 'c', 'aa']

def rle(tab:list):
    rle_ret = []
    for elt in tab:

        if len(rle_ret) == 0:           # --> Premier élément
            rle_ret.append((1, elt))
            continue
        
        if rle_ret[-1][1] == elt:       # --> Si le dernier élément est le même (incrément)
            rle_ret[-1] = (rle_ret[-1][0]+1, rle_ret[-1][1])
        else:                           # --> Sinon (ajout)
            rle_ret.append((1, elt))

    return rle_ret

def inv_rle(tab:list):
    inv_rle_ret = []
    for numb, thing in tab: 
        for i in range(numb): inv_rle_ret.append(thing)
    return inv_rle_ret

print(rle(t), inv_rle(rle(t)))