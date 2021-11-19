#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = list()
    for i in my_list:
        if i % 2 == 0:
            a.append(True)
        else:
            a.append(False)
    return a
