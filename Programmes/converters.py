from math import log2

def b2d(binary_number:int) -> int:
    for i in str(binary_number):
        if i!='1' and i!= '0':
            return ValueError
    decimal_number = 0
    binary_number_str = str(binary_number)
    for i in range(len(str(binary_number))):
        decimal_number += (2**i) * int(binary_number_str[len(binary_number_str) - i -1])
    return decimal_number


def d2b(decimal_number:int)->int:
    return_string = ""
    for i in range(int(log2(decimal_number)), -1, -1):
        if decimal_number - 2**i >= 0:
            return_string += "1"
            decimal_number -= 2**i
        else:
            return_string += "0"
    return return_string


def b2hex(binary_number:str)->str:
    return decimal_to_another(b2d(binary_number))

def decimal_to_another(decimal_number:int, base:int | None = 16)->str:
    if base > 16 or base < 1:
        raise ValueError('Base is incorrect')
    hex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    return_string = ""
    while decimal_number !=0:
        return_string = str(hex_list[decimal_number%base]) + return_string
        decimal_number //= base
    return return_string


def hex2decimal(hex_num:str):
    hex_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'a', 'b', 'c', 'd', 'e', 'f']
    return_int = 0
    for i in range(len(hex_num)):
        return_int += hex_list.index(hex_num[i]) * (16 ** (len(hex_num)-i-1))
    
    return return_int



print(hex2decimal("4e5b"))