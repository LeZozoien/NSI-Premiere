def sort_list(to_sort):
    while True:
        flag = 1
        for i in range(len(to_sort) - 1):
            if to_sort[i] > to_sort[i + 1]:
                to_sort[i], to_sort[i + 1] = to_sort[i + 1], to_sort[i]
        while i < len(to_sort):
            if(to_sort[i] < to_sort[i - 1]):
                flag = 0
            i += 1
        if flag == 1:
            break
    return to_sort

all_of_them = []

for i in range(2, 101):
    for j in range(2, 101):
        all_of_them.append(i**j)

all_of_them = sorted(all_of_them)


for i in range(len(all_of_them)-1, 0, -1):
    if all_of_them[i] == all_of_them[i-1]:
        all_of_them.pop(i-1)

print(all_of_them, len(all_of_them))