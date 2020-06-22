"""
Program: average_scores_kwargs.py
Author: Ryan Elliott
Last date modified: 06/21/2020
This program uses args and kwargs to output a string with different values
Input average scores and information
Outputs string with all information appended
"""


def average_scores(*args, **kwargs):
    """Returns string with all information and calculated GPA
    :param args the users scores
    :param kwargs the users information
    :returns output, string with all information and GPA
    """
    total = 0
    count = 0
    output = ''
    for num in args:
        total += num
        count += 1
    for key, value in kwargs.items():
        output += ("%s = %s " % (key, value))

    output += "GPA = " + str((total / count))
    return output


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, first_name='Michelle', last_name='Ruse', major='World_domination'))
    print(average_scores(4, 4, 1, Name='Michelle', LName='Ruse'))
    print(average_scores(4, 3, 2, 4, 4, 1, Name='Michelle', LName='Ruse', major='Science', school='UI'))
