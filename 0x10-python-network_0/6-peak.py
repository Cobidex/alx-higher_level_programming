#!/usr/bin/python3
'''finds a peak in a list of integers'''


def find_peak(list_of_integers):
    '''function tto find the peak'''
    if len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid = (len(list_of_integers) - 1) // 2

    if mid == 0:
        if list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[mid]
        else:
            return list_of_integers[mid + 1]

    if mid == (len(list_of_integers) - 1):
        if list_of_integers[mid] >= list_of_integers[mid - 1]:
            return list_of_integers[mid]
        else:
            return list_of_integers[mid - 1]

    left = find_peak(list_of_integers[:mid])
    right = find_peak(list_of_integers[mid:])

    if left < right:
        return right
    else:
        return left
