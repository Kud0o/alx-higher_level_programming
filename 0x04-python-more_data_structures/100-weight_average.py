#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        i1 = sum(list(map(lambda x: x[0] * x[1], my_list)))
        i2 = sum(list(map(lambda x: x[1], my_list)))
        return i1 / i2
    else:
        return 0
