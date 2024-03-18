def Champernowne(x:int):
    a = "0."
    i = 1
    while len(a)-2 < x:
        a += str(i)
        i += 1
    return(a[x+1])

result = 1
for i in range(7):
    result *= int(Champernowne(10**i))

print(result)