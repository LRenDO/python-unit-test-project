# Group 24
# CS362 Summer 2021
# Due Date: 2021-08-09


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
