#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    mid = len(list_of_integers) // 2
    peak = list_of_integers[mid]

    if (mid == 0 or peak >= list_of_integers[mid - 1]) and \
       (mid == len(list_of_integers) - 1 or peak >= list_of_integers[mid + 1]):
        return peak

    if mid > 0 and peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
