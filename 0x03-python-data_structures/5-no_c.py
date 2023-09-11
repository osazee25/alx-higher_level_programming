#!/usr/bin/python3
def no_c(my_string):
    my_list = [i for i in my_string if i not in ('c', 'C')]
    item = "".join(my_list)
    return item
