all_results = {}

def collatz(x:int)->int:
    sequence = ""
    number = x
    global all_results
    iterations = 0
    while x != 1:
        iterations += 1
        if x%3 == 0:
            x /= 3
            sequence += "D"
            if x in all_results:
                all_results[number] = sequence + all_results[x]
                return sequence + all_results[x]
        elif x%3 == 1:
            x = (4*x + 2)/3
            sequence += "U"
            if x in all_results:
                all_results[number] = sequence + all_results[x]
                return sequence + all_results[x]
        else:
            x = (2*x-1)/3
            sequence += "d"
            if x in all_results:
                all_results[number] = sequence + all_results[x]
                return sequence + all_results[x]
    all_results[number] = sequence
    return sequence


def calc_with_sequence(sequence:str):
    if len(sequence) % 2 == 0:
        for i in range(int(len(sequence)/2)):
            sequence[i], sequence[-1 * (i+1)] = sequence[-1 * (i+1)], sequence[i]
    else:
        for i in range(int(len(sequence)/2-0.5)):
            sequence[i], sequence[-1 * (i+1)] = sequence[-1 * (i+1)], sequence[i] 
    result = 1
    for letter in sequence:
        if letter == "D":
            result *= 3
        elif letter == "d":
            result *= 3
            result += 1
            result /= 2
        else:
            result *= 3
            result -= 2
            result /= 4
    return result


print(calc_with_sequence("UDDDUdddDDUDDddDdDddDDUDDdUUDd"))