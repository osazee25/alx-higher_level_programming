#!/usr/bin/python3
for tens in range(10):
    for unit in range(tens + 1, 10):
        print("{}{}".format(tens, unit), end=', ' if ((tens * 10) + unit) < 89 else '\n')
