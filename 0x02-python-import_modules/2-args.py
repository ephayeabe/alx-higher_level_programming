#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv)
    if size-1 == 1:
        print("{:d} argument".format(size - 1), end="")
    else:
        print("{:d} arguments".format(size - 1), end="")
    if size - 1 == 0:
        print(".")
    else:
        print(":")
    for i in range(1, size):
        print("{:d}: {:s}".format(i, sys.argv[i]))
