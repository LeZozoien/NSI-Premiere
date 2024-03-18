t = [1000, 800, 802, 1000, 1003]

def encode(tab:list)->list:
    ret = []
    ret.append(tab[0])
    for i in range(1, len(tab)):
        ret.append(tab[i]-tab[i-1])
    return ret

def decode(tab:list):
    ret = []
    ret.append(tab[0])
    for i in range(1, len(tab)):
        ret.append(tab[i]+ret[i-1])
    return ret

print(encode(t), decode(encode(t)))

