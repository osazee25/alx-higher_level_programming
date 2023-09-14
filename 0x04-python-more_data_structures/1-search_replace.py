#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if search == j else j for j in my_list]
