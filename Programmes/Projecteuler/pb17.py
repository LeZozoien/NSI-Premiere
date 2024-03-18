significations = {1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five",
                  6 : "six", 7 : "seven", 8 : "eight", 9 : "nine", 10 : "ten",
                  11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen",
                  16 : "sixteen", 17 : "seventeen", 18 : "eighteen", 19 : "nineteen",
                  20 : "twenty", 30 : "thirty", 40 : "forty", 50 : "fifty",
                  60 : "sixty", 70 : "seventy", 80 : "eighty", 90 : "ninety", 100 : "hundred",
                  1000 : "thousand"}


def name(x:int)->str:
    to_return = ""
    if x >= 1000:
        if x//1000 > 1:
            to_return += significations[x//1000] + " thousand"
            x -= (x//1000) * 1000
        else:
            to_return += "one thousand"
            x -= 1000
        if x > 0:
                to_return += " "
    if x >= 100:
        to_return += significations[x//100]+" "+significations[100]
        x -= (x//100)*100
        if x>0:
            to_return += " and "
    if x >=20:
        to_return += significations[(x//10)*10]
        x -= (x//10)*10
        if x>0:
            to_return += " "
    if x>0:
        to_return += significations[x]
    return to_return

maximumlengthstring = ""

for i in range(2000):
    i += 1
    maximumlengthstring += name(i)
    print(i, name(i))

print(len(maximumlengthstring))