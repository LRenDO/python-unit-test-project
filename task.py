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
    if num_string == '' or type(num_string) is not str:
        return None

    num_string = num_string.upper()

    if is_valid(num_string):
        if num_string[:2] == '0X' or num_string[:3] == '-0X':
            return conv_hex(num_string)

        elif num_string.find('.') != -1:
            return conv_float(num_string)

        return conv_int(num_string)
    else:
        return


def is_valid(num_string):
    """
    Checks string to make sure it is valid

    Parameter: num_string (string) number to be checked
    Returns: True if valid. Otherwise False.
    """

    decimal_index = num_string.find('.')
    if decimal_index != -1 and decimal_index != len(num_string) - 1:
        if num_string[decimal_index + 1:].find('.') != -1:
            return False

    if num_string.isupper():
        for char in num_string:
            if not valid_hex_chr(char):
                return False
        if num_string[:2] != "0X" and num_string[:3] != "-0X":
            return False

    return True


def valid_hex_chr(char):
    """
    Converts strings of numbers without decimal point into integers

    Parameter: char (character) to be compared
    Returns: True if valid hex char. Otherwise False.
    """
    if char == '-' or char == 'X':
        return True

    if ord(char) >= ord('0'):
        if ord(char) <= ord('9'):
            return True

    if ord(char) >= ord('A'):
        if ord(char) <= ord('F'):
            return True

    return False


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
        if decimal_index == 0:
            left_side = 0
        else:
            left_side = conv_int(num_string[:decimal_index])
        right_str = num_string[decimal_index + 1:]
        right_side = conv_int(right_str) * pow(10, -len(right_str))
        return left_side + right_side


def conv_hex(num_string):
    """
    Converts strings of hex numbers with prefix 0x into base 10 integer

    Parameter: num_string (string) number to be converted
    Returns: base 10 integer
    """
    if num_string[0] == '-':
        if num_string == '-0X0':
            return 0
        else:
            return -conv_hex(num_string[3:])

    if num_string[:2] == '0X':
        num_string = num_string[2:]

    num = 0
    exp = 0
    for char in reversed(num_string):
        if char.isupper():
            digit = ord(char) - ord('A') + 10
        else:
            digit = ord(char) - ord('0')
        num = num + digit * pow(16, exp)
        exp += 1
    return num

