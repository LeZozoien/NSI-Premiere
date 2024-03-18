a = []
for i in range(1010):
    i += 1
    for j in range(1010-i):
        j += 1
        if ((i**2 + j**2)**0.5)%1 == 0:
            a.append([i, j, int(((i**2 + j**2)**0.5))])



for k in a:
    if k[0]+k[1]+k[2]==1000:
        print(k[0], k[1], k[2])