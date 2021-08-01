# Task Functions (Group Project)
# Authors: Lauren "Ren" Demeis-Ortiz, William Wells, Louis Adams (Group 24)
# Description: Contains functions. The first converts strings to numbers. The
#              second converts number of seconds since Jan. 1 1970 to date and
#              time. The last one takes an integer and converts it to hex in
#              in big endian or little endian.

def conv_num(num_string):
    """
    Converts strings into numbers

    Parameter: num_string (string) number to be converted. Can be integer,
        decimal or hex (must be in 0x or -0x prefix format)
    Returns: integer or float
    """
    if num_string.find('.') != -1:
        return conv_float(num_string)

    return conv_int(num_string)


def conv_int(num_string):
    """
    Converts strings of numbers without decimal point into integers

    Parameter: num_string (string) number to be converted
    Returns: integer
    """
    if num_string[0] == '-':
        return -conv_int(num_string[1:len(num_string)])

    num = 0
    exp = 0
    for char in reversed(num_string):
        digit = ord(char) - ord('0')
        num = num + digit * pow(10, exp)
        exp += 1
    return num


def conv_float(num_string):
    """
    Converts strings of positive numbers containing decimal point into float

    Parameter: num_string (string) number to be converted must contain a
        decimal point
    Returns: float
    """
    if num_string[len(num_string) - 1] == '.':
        num_string = num_string + '0'

    if num_string[0] == '-':
        return -conv_float(num_string[1:len(num_string)])

    else:
        decimal_index = num_string.find('.')
        left_side = conv_int(num_string[0:decimal_index])
        right_str = num_string[decimal_index + 1:len(num_string)]
        right_side = conv_int(right_str) * pow(10, -len(right_str))
        return left_side + right_side
