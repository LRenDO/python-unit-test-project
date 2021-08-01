# task functions
# Authors: Lauren "Ren" Demeis-Ortiz, William Wells, Louis Adams
# Description: Contains functions. The first converts strings to numbers. The
#              second converts number of seconds since Jan. 1 1970 to date and
#              time. The last one

def conv_num(num_string):
    """
    Converts strings into numbers

    Parameter: num_string (string) number to be converted
    Returns: integer, float or hexadecimal
    """
    if num_string[0] == '-':
        num = conv_negative_int(num_string)
    else:
        num = conv_positive_int(num_string)
    return num


def conv_negative_int(num_string):
    """
    Converts strings of negative numbers into integers

    Parameter: num_string (string) number to be converted must be positive
    Returns: integer
    """
    num = 0 - conv_positive_int(num_string[1:len(num_string)])
    return num


def conv_positive_int(num_string):
    """
    Converts strings of positive numbers into integers

    Parameter: num_string (string) number to be converted must be positive
    Returns: integer
    """
    num = 0
    exp = 0
    for char in reversed(num_string):
        digit = ord(char) - ord('0')
        num = num + digit * pow(10, exp)
        exp += 1
    return num
