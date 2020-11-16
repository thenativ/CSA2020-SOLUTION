#!/usr/bin/python
import math
import time

with open("a.dat", "r") as f:
    a = [int(x) for x in f.read().strip(' ').split(',')]


def f_arr_add(arr, offset_min, offset_max, value):
        for i in range(offset_min, offset_max):
            arr[i] += value

def f_arr_sub(arr, offset_min, offset_max, value):
    for i in range(offset_min, offset_max):
        arr[i] -= value

def f_arr_xor(arr, offset_min, offset_max, value):
    for i in range(offset_min, offset_max):
        arr[i] = arr[i] ^ value

def f_arr_print(arr, offset):
    result_string = ""
    for i in range(0, arr[offset + 1]):
        result_string += str(chr(arr[offset + 2 +i] ^ 0x37))
    return result_string

f_list = [f_arr_add, f_arr_sub, f_arr_xor]

start_char = 'A'
string = start_char * 42
b = [ord(c) for c in string]
final = [x for x in b]
result = ""

###################################################

def decrypt(a):
    i = 0
    division_arr = []
    final = []

    for j in range(0,42):
        final.append([])

    while (i < len(a)) :
        val_0 = a[i]
    
        if (val_0 == 5) :
            result = f_arr_print(a, i)
            break
           
        val_1 = a[i+1]
        val_2 = a[i+2]
        val_3 = a[i+3]

        if val_3 == 17251:
            while ((b[val_1] % val_2 == 0) == (4-val_0)):
                b[val_1]+=1

        division_arr.append([val_1,val_2,4-val_0])

        if ((b[val_1] % val_2 == 0) == (4-val_0)) :
            i = val_3
            continue
        
        if not (b[val_1] % val_2):
            b[val_1] = int(math.floor(b[val_1]/val_2))

        val_4 = a[i+4]
        val_5 = a[i+5]
        val_6 = a[i+6] ^ val_0-3
        f_val = a[val_6]
        f_list[val_4](a, i+7, (val_5+1)*7, f_val)
        i += 7
    
    for s in division_arr:
        if s[2] == 0:
            final[s[0]].append(s[1])

    decoded = ""
    for x in final:
        tmp = 1
        for n in x:
            tmp*=n
        decoded += chr(tmp)
    print(decoded) 

###################################

decrypt(a)
