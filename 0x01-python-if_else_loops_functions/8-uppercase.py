#!/usr/bin/python3
def upper_conv(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return (ord(char) - 32)
    else:
        return ord(char)

def uppercase(string):
    string_upper = ""
    for char in string:
        string_upper += "%c" % upper_conv(char)
    print("{:s}".format(string_upper))
