#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv)
    sum = 0
    for i in range(1, size):
        sum += int(sys.argv[i])
    print(sum)
