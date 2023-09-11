#!/usr/bin/python3
def div_2(num):
    if num % 2 == 0:
        return True
    else:
        return False


def divisible_by_2(my_list=[]):
    return ([div_2(i) for i in my_list])
