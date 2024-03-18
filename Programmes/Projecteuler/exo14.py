all_results = {}

def collatz(x:int)->int:
    number = x
    global all_results
    iterations = 0
    while x != 1:
        iterations += 1
        if x%2 == 0:
            x /= 2
            if x in all_results:
                all_results[number] = all_results[x] + iterations
                return all_results[x] + iterations
        else:
            x = 3*x + 1
    all_results[number] = iterations
    return iterations

for i in range(1, 10000000):
    collatz(i)

print(all_results)