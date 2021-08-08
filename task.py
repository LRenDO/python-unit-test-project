# Task Functions (Group Project)
# Class: CS362 Summer 2021
# Due Date: 2021-08-09
# Authors: Lauren "Ren" Demeis-Ortiz, William Wells, Louis Adams (Group 24)
# Description: Contains functions. The first converts strings to numbers. The
#              second converts number of seconds since Jan. 1 1970 to date and
#              time. The last one takes an integer and converts it to hex in
#              in big endian or little endian.


# -----------------------------------------------------------------------------
# Function 1
# -----------------------------------------------------------------------------
def conv_num(num_string):
    """
    Converts strings into numbers

    Parameter: num_string (string) number to be converted. Can be integer,
        decimal or hex (must be in 0x or -0x prefix format)
    Returns: integer or float
    """
    # Check for empty string or non string type
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
    # Check for symbols and prefixes with no numbers
    no_number = ['.', '-', '0X', '-0X']
    if num_string in no_number:
        return False

    # Check for more than one decimal point
    # Finds index of first decimal and checks remainder of string for a second
    decimal_index = num_string.find('.')
    if decimal_index != -1 and decimal_index + 1 != len(num_string):
        if num_string[decimal_index + 1:].find('.') != -1:
            return False

    # Check for valid hex digits and prefixes
    if num_string.isupper():
        # Check valid hex character
        for char in num_string:
            if not valid_hex_chr(char):
                return False
        # Check valid prefix
        if num_string[:2] != "0X" and num_string[:3] != "-0X":
            return False

    return True


def valid_hex_chr(char):
    """
    Converts strings of numbers without decimal point into integers

    Parameter: char (character) to be compared
    Returns: True if valid hex char. Otherwise False.
    """
    # Check if hex prefix character
    if char == '-' or char == 'X':
        return True

    # Check if digit
    if ord(char) >= ord('0'):
        if ord(char) <= ord('9'):
            return True

    # Check if hex letter
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
        return -conv_int(num_string[1:])

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
    if num_string[-1] == '.':
        num_string = num_string + '0'

    if num_string[0] == '-':
        return -conv_float(num_string[1:])

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


# -----------------------------------------------------------------------------
# Function 2
# -----------------------------------------------------------------------------
def is_leap_year(year):
    """Returns whether or not the given year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def my_datetime(num_sec):
    """Converts the given integer of seconds since the Unix epoch and returns
    it as a date string in the format "MM-DD-YYYY".
    """
    month, day, year = 1, 1, 1970

    # Reduce time to number of remaining days (60 * 60 * 24)
    remaining_days = num_sec // 86400

    while remaining_days >= 365:
        remaining_days -= 366 if is_leap_year(year) else 365
        year += 1

    # Map months to their days by index
    month_days = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        month_days[2] = 29

    while remaining_days >= month_days[month]:
        remaining_days -= month_days[month]
        month += 1

    day += remaining_days

    return f'{month:02}-{day:02}-{year}'


# -----------------------------------------------------------------------------
# Function 3
# -----------------------------------------------------------------------------
def reverse_endianness(hex_str):
    """This function reverses a little endian hexadecimal byte string to big
    endian or vice versa

    :param hex_str: a string of hexadecimal bytes separated by spaces
    :return: a string of hexadecimal bytes separated by spaces of the opposite
        endianness
    """
    i = 0
    j = 1
    m = len(hex_str) - 2
    n = len(hex_str) - 1
    new_str = list(hex_str)

    while(i <= m):
        new_str[i] = hex_str[m]
        new_str[j] = hex_str[n]
        new_str[m] = hex_str[i]
        new_str[n] = hex_str[j]
        i += 3
        j += 3
        m -= 3
        n -= 3

    new_str = ''.join(new_str)

    return new_str


def conv_endian(num, endian='big'):
    """This function converts a decimal integer to a string of hexadecimal
    bytes

    :param num: a decimal integer to be converted to hexadecimal bytes
    :param endian: can be 'big' or 'little', 'big' is the default if not
                   supplied
    :return: a string of hexadecimal bytes in big or little endian form
             separated by spaces, may include a negative sign

    adapted from:
    https://pencilprogrammer.com/python-programs/convert-decimal-to-hexadecimal
    """
    if endian != 'big' and endian != 'little':
        return None

    if num == 0:
        return '00'

    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B',
                  'C', 'D', 'E', 'F']
    decimal = abs(num)
    hex_str = ''

    # each byte is made up of 2 hex digits, digit_num keeps track of which
    # digit we are currently on
    digit_num = 0

    while(decimal > 0):
        remainder = decimal % 16
        hex_str = hex_digits[remainder] + hex_str
        digit_num += 1
        decimal = decimal // 16
        if digit_num == 2 and decimal != 0:     # add a space only if we have
            hex_str = ' ' + hex_str             # finished a byte and have more
            digit_num = 0                       # bytes to write

    if digit_num == 1:                          # fill out the final byte with
        hex_str = '0' + hex_str                 # an initial zero if necessary

    if endian == 'little':
        hex_str = reverse_endianness(hex_str)

    if num < 0:
        hex_str = '-' + hex_str

    return hex_str
