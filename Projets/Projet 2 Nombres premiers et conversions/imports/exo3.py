def crible(n:int)->list[bool]:
    primes = [True for i in range(n)]

    primes[0], primes[1] = False, False

    for i in range(2, int(n/2)):
        for k in range(2, int(n/i)+1):
            try:
                primes[k * i] = False
            except:
                pass
        if i%1 == 0:
            print(i)

    return(primes)



primes = crible(10000000)
print("fini")