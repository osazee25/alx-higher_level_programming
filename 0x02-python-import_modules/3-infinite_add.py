#!/usr/bin/python3
def sum_arg(argv):
    x = len(argv) - 1
    if x == 0:
        print("{:d} argument".format(x))
        return
    else:
        j = 1
        add = 0
        while j <= x:
            add += int(argv[j])
            j += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    sum_arg(sys.argv)
