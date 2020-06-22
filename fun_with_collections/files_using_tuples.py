"""
Program: files_using_tuples.py
Author: Ryan Elliott
Last date modified: 06/21/2020
This program allows the user to enter a students name and then test scores, this information is written to a file
Input student name and test scores
Outputs the file with all student names and scores
"""
import os as os


def write_to_file(*args):
    """Writes the tuple with students name and scores to the file
    :param *args, tuple with student name and scores
    """
    f = open('student_info.txt', 'a')
    f.write("\n" + str(args))
    f.close()


def get_student_info(s_name):
    """Takes users input of s_name and adds scores to tuple
    :param s_name
    :returns tuple to write_to_file()
    """
    numbers = ()
    numbers = numbers + (s_name,)
    exit_loop = False
    print("Enter test scores, enter '0' when you are finished.")
    userNum = int(input())
    while userNum != 0:
        while userNum < 1 or userNum > 100:
            print("Please enter a value between 1-100")
            print("Enter numbers from 1-100, enter '0' when you are finished.")
            userNum = int(input())
            if userNum == 0:
                exit_loop = True
            break
        if exit_loop:
            break
        numbers = numbers + (userNum, )
        print("Enter numbers from 1-100, enter '0' when you are finished.")
        userNum = int(input())
    write_to_file(numbers)


def read_from_file():
    """Reads the 'student_info.txt' file
    """
    file_dir = os.path.dirname(__file__)
    file_name = "student_info.txt"
    f = open(os.path.join(file_dir, file_name), "r")
    line = f.read()
    print(line)
    f.close()


if __name__ == '__main__':
    print("Enter a students name, enter 'stop' when you are finished.")
    st_name = input()
    while st_name != 'stop':
        get_student_info(str(st_name))
        read_from_file()
        print("Enter a students name, enter '0' when you are finished.")
        st_name = input()
