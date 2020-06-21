"""
Program: basic_list.py
Author: Ryan Elliott
Last date modified: 06/21/2020
This program asks the user to input 3 numbers and then creates a list
Input numbers
Outputs the created list
"""


def make_list():
    """Returns the created list
    :returns full_list
    """
    full_list = []
    for x in range(3):
        full_list.append(get_input())
    return full_list


def get_input():
    """Returns the users input
    :returns num
    """
    try:
        num = int(input("Enter a number: "))
    except ValueError as err:
        print("ValueError encountered")
    else:
        return num


if __name__ == '__main__':
    try:
        print(make_list())
    except ValueError as err:
        print("ValueError encountered")
