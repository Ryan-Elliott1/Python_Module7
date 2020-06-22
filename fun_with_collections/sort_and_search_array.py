"""
Program: sort_and_search_array.py
Author: Ryan Elliott
Last date modified: 06/21/2020

"""
import array as arr


def search_array(a_array, obj_look):
    try:
        obj_index = a_array.index(obj_look)
    except ValueError as err:
        return -1
    else:
        return obj_index


def sort_array(a_array):
    pass


if __name__ == '__main__':
    numbers = [3, 2, 5]
    numbers_array = arr.array('i', numbers)
    print(search_array(numbers_array, 5))
