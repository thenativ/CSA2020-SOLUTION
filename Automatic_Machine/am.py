#!/usr/env/python3
import math

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

def encryption_main(machine_arr, password_arr):
    i = 0
    res = [x for x in password_arr]
    while i < len(machine_arr):
        val_0 = machine_arr[i]
    
        if val_0 == 5:
            print("".join(chr(c) for c in res))
            print(password_arr)
            return f_arr_print(machine_arr, i)
            break
    
        val_1 = machine_arr[i+1]
        val_2 = machine_arr[i+2]
        val_3 = machine_arr[i+3]
           
        ### BYPASS ###
        while ((password_arr[val_1] % val_2 == 0) == (4 - val_0)) and val_3 == 17251:
            password_arr[val_1] += 1
            res[val_1] += 1
        ##############
                
        if ((password_arr[val_1] % val_2 == 0) == (4 - val_0)):
            i = val_3
            continue

        if (password_arr[val_1] % val_2) == 0:
            password_arr[val_1] = math.floor(password_arr[val_1]/val_2)
            res[val_1] *= val_2

        val_4 = machine_arr[i+4]
        val_5 = machine_arr[i+5]
        val_6 = machine_arr[i+6]
        f_val = machine_arr[val_6 ^ (val_0-3)]
        f_list[val_4](machine_arr, i+7, (val_5+1)*7, f_val)
        i+= 7

        print("i = " + str(i-7)
                + "\nval_0 = " + str(val_0)
                + "\nval_1 = " + str(val_1)
                + "\nval_2 = " + str(val_2)
                + "\nval_3 = " + str(val_3)
                + "\nval_4 = " + str(val_4)
                + "\nval_5 = " + str(val_5)
                + "\nval_6 = " + str(val_6)
                + "\nPASSWORD = " + "".join(chr(c) for c in password_arr))
        


password = [ord(x) for x in ("A"*42)]
print(encryption_main(a,password))
