#!/usr/bin/python3

def upper_conv(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return chr(ord(char) - 32)  # Convert to uppercase and return the character
    else:
        return char  # If not a lowercase letter, return the character as is

def uppercase(string):
    string_upper = ""
    for char in string:
        string_upper += upper_conv(char)
    print("{:s}".format(string_upper))
