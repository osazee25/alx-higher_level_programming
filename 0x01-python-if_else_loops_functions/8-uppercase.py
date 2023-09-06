#!/usr/bin/python3
def uper_conv(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return (ord(char) - 32)
    else:
        return ord(char)


def uppercase(string):
    string_uper = ""
    for character in string:
        string_uper += "%c" % uper_conv(character)
    print("{:s}".format(string_uper))
