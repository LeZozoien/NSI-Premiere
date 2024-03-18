def gen_tri_num(x:int) -> int:
    return int((x**2 + x)/2)


diviseurs = 0
i = 1
max_diviseurs = 0

while diviseurs < 500:
    a_tester = gen_tri_num(i)
    diviseurs = 0
    for j in range(int((a_tester**0.5)+1)):
        if a_tester%(j+1) == 0:
            if (j+1)**2 == a_tester:
                diviseurs += 1
            else:
                diviseurs += 2

    i += 1
    if diviseurs > max_diviseurs:
        print(i, diviseurs, a_tester)
        max_diviseurs = diviseurs
    