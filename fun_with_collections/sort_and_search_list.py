"""
Program: sort_and_search.py
Author: Ryan Elliott
Last date modified: 06/21/2020
This program searches for an object in a list and returns the index and sorts the list
Input list and the object to search for or the list to sort
Returns the object index or sorted list
"""


def search_list(a_list, obj_look):
    """Returns index if object is present or -1 is not found
    :param a_list the users list
    :param obj_look the object to search for
    :returns object_index or -1
    """
    try:
        obj_index = a_list.index(obj_look)
    except ValueError as err:
        return -1
    else:
        return obj_index


def sort_list(a_list):
    pass


if __name__ == '__main__':
    ab_list = [3, 2, 5]
    print(search_list(ab_list, 4))
