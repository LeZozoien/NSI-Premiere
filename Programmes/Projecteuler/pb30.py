a = []

for i in range(10,1000000):
    i = str(i)
    thing = 0
    for k in range(len(i)):
        thing += (int(i[k])**5)
    if thing == int(i):
        a.append(int(i))
print(a)
print(sum(a))