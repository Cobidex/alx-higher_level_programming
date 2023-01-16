#!/usr/bin/python3
'''finds the peak element'''

def find_peak(list_of_integers):
    '''finds the peak element'''

    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    peak = list_of_integers[0]
    for i in range(0, len(list_of_integers) - 1):
        if list_of_integers[i] <= list_of_integers[i + 1]:
            peak = list_of_integers[i + 1]
    return peak
