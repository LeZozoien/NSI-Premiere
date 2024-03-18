maximum = 0
def is_palindrome(x):
    palindrome = True
    if len(x)%2 == 0:
        for i in range(int(len(x)/2)):
            if x[i] != x[len(x)-i-1]:
                palindrome = False
    else:
        for i in range(int(len(x)/2 - 0.5)):
            if x[i] != x[len(x)-i-1]:
                palindrome = False
    return(palindrome)


for k in range(1000):
    for l in range(1000):
        if is_palindrome(str(k*l)) and k*l > maximum:
            maximum = k*l

print(maximum)