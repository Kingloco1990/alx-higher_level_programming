#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    Return a peak in a list of unsorted integers.

    A peak is defined as an element in the list that is greater than or equal
    to its neighbors. This function uses a divide-and-conquer approach to
    efficiently find a peak in the list.

    Args:
        list_of_integers (list): The list of unsorted integers.

    Returns:
        int or None: The peak element in the list,
        or None if the list is empty.
    """
    # Check if the list is empty
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    # If there's only one element in the list, it is a peak
    if size == 1:
        return list_of_integers[0]
    # If there are only two elements, return the maximum
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peak = list_of_integers[mid]
    # Check if the middle element is a peak
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    # If not, recursively search for a peak in the left half
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    # Otherwise, recursively search for a peak in the right half
    else:
        return find_peak(list_of_integers[mid + 1:])
