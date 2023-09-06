#!/usr/bin/python3
comb = 0
while comb <= 89:
    if comb % 10 == 0:
        comb += 1 + comb // 10
    print("{:02d}".format(comb), end='\n' if comb == 89 else ", ")
    comb += 1
