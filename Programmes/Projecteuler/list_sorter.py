def sort_list1(to_sort):
    while True:
        flag = 1
        for i in range(len(to_sort) - 1):
            if to_sort[i] > to_sort[i + 1]:
                to_sort[i], to_sort[i + 1] = to_sort[i + 1], to_sort[i]
        for i in range(2, len(to_sort)):
            if(to_sort[i] < to_sort[i - 1]):
                flag = 0
        if flag == 1:
            break
    return to_sort

def sort_list2(to_sort):
    temp = []
    while(len(to_sort>0)):
        for i in to_sort:
            pass

    return temp

print(sort_list1([1, 9, 7, 3, 6]))