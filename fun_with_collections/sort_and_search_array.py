"""
Program: sort_and_search_array.py
Author: Ryan Elliott
Last date modified: 06/21/2020
This program searches for an object in an array and returns the index and sorts the array
Input array and the object to search for or the array to sort
Returns the object index or sorted array
"""
import array as arr


def search_array(a_array, obj_look):
    """Returns index if object is present or -1 is not found
    :param a_array the users array
    :param obj_look the object to search for
    :returns object_index or -1
    """
    try:
        obj_index = a_array.index(obj_look)
    except ValueError as err:
        return -1
    else:
        return obj_index


def sort_array(a_array):
    """Returns the sorted array
    :param a_array the users array
    :returns a_array after being sorted
    """
    for x in range(3):
        for y in range(3):
            if a_array[x] < a_array[y]:
                temp = a_array[x]
                a_array[x] = a_array[y]
                a_array[y] = temp
    return a_array


if __name__ == '__main__':
    numbers = [3, 2, 5]
    numbers_array = arr.array("i", numbers)
    print(search_array(numbers_array, 5))
    print(sort_array(numbers_array))
