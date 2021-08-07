import unittest
import task


class TestCase(unittest.TestCase):
    # -------------------------------------------------------------------------
    # Function 1 Tests
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Tests for Conversion to Integer conv_num()
    # -------------------------------------------------------------------------
    # Tests type for int
    def test_conv_num_int_type(self):
        test_case = '-219'
        expected = type(-219)
        self.assertEqual(type(task.conv_num(test_case)), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests conversion to int 0
    def test_conv_num_int_0(self):
        test_case = '0'
        expected = 0
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests conversion to int 219
    def test_conv_num_int_pos(self):
        test_case = '219'
        expected = 219
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests conversion to int -10
    def test_conv_num_int_neg(self):
        test_case = '-910'
        expected = -910
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # -------------------------------------------------------------------------
    # Tests for Conversion to Float
    # -------------------------------------------------------------------------
    # Tests type for float
    def test_conv_num_float_type(self):
        test_case = '-219.'
        expected = type(-219.0)
        self.assertEqual(type(task.conv_num(test_case)), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests conversion to float 0
    def test_conv_num_float_0(self):
        test_case = '0'
        expected = 0
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests conversion to float with no digit after decimal point
    def test_conv_num_no_right(self):
        test_case = '12345.'
        expected = 12345.0
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests conversion to float with no digit before decimal point
    def test_conv_num_no_left(self):
        test_case = '.45'
        expected = 0.45
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests conversion to float 1589.03950
    def test_conv_num_float_pos(self):
        test_case = '1589.03950'
        expected = 1589.03950
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests conversion to float -1589.03950
    def test_conv_num_float_neg(self):
        test_case = '-1589.03959'
        expected = -1589.03959
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # -------------------------------------------------------------------------
    # Tests for Hex Conversion to Base 10 Integer
    # -------------------------------------------------------------------------
    # Tests type for Hex
    def test_conv_num_hex_type(self):
        test_case = '-0xf52C'
        expected = type(-2772)
        self.assertEqual(type(task.conv_num(test_case)), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests hex conversion to base 10 0x0
    def test_conv_num_hex_0(self):
        test_case = '0x0'
        expected = 0
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests hex conversion to base 10 0x0
    def test_conv_num_hex_neg0(self):
        test_case = '-0x0'
        expected = 0
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests hex conversion to base 10 0xaD4
    def test_conv_num_hex_pos(self):
        test_case = '0xaD4'
        expected = 2772
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests hex conversion to base 10 -0xf52C
    def test_conv_num_hex_neg(self):
        test_case = '-0xaD4'
        expected = -2772
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # -------------------------------------------------------------------------
    # Tests Invalid Inputs Return None
    # -------------------------------------------------------------------------
    # Tests empty string
    def test_conv_num_empty(self):
        test_case = ''
        expected = None
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests more than one decimal point on ends
    def test_conv_num_decimal(self):
        test_case = '.234.'
        expected = None
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests more than one decimal point in center
    def test_conv_num_decimal_center(self):
        test_case = '.23.4.'
        expected = None
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests invalid characters
    def test_conv_num_symbols(self):
        test_case = '0x2a@3'
        expected = None
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests invalid characters
    def test_conv_num_g(self):
        test_case = '0x2aG3'
        expected = None
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests hex string with out 0x prefix
    def test_conv_num_no_prefix(self):
        test_case = '2af3'
        expected = None
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests non-string types
    def test_conv_num_type(self):
        test_case = 2459
        expected = None
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests - symbol only
    def test_conv_num_neg_sign(self):
        test_case = '-'
        expected = None
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests . symbol only
    def test_conv_num_point_only(self):
        test_case = '.'
        expected = None
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests 0x hex prefix only
    def test_conv_num_prefix(self):
        test_case = '0x'
        expected = None
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests -0x hex prefix only
    def test_conv_num_neg_prefix(self):
        test_case = '-0x'
        expected = None
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # -------------------------------------------------------------------------
    # Function 2 Tests
    # -------------------------------------------------------------------------
    def test_my_datetime_initial(self):
        self.assertEqual(task.my_datetime(0), '01-01-1970')

    # -------------------------------------------------------------------------
    # Function 3 Tests
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Tests for Conversion to Big Endian
    # -------------------------------------------------------------------------
    # convert zero to big endian
    def test201(self):
        num = 0
        endian = 'big'
        self.assertEqual(task.conv_endian(num, endian), '00',
                         msg='Does not pass (num={})'.format(num))

    # convert a positive int to big endian
    def test202(self):
        num = 954786
        endian = 'big'
        self.assertEqual(task.conv_endian(num, endian), '0E 91 A2',
                         msg='Does not pass (num={})'.format(num))

    # convert a positive int with the endian argument omitted
    def test203(self):
        num = 954786
        self.assertEqual(task.conv_endian(num), '0E 91 A2',
                         msg='Does not pass (num={})'.format(num))

    # convert a negative int to big endian
    def test204(self):
        num = -954786
        endian = 'big'
        self.assertEqual(task.conv_endian(num, endian), '-0E 91 A2',
                         msg='Does not pass (num={})'.format(num))

    # convert a small positive int to big endian
    def test205(self):
        num = 6
        endian = 'big'
        self.assertEqual(task.conv_endian(num, endian), '06',
                         msg='Does not pass (num={})'.format(num))

    # convert a small negative int to big endian
    def test206(self):
        num = -6
        endian = 'big'
        self.assertEqual(task.conv_endian(num, endian), '-06',
                         msg='Does not pass (num={})'.format(num))

    # convert a large positive int to big endian
    def test207(self):
        num = 123456789987654321
        endian = 'big'
        self.assertEqual(task.conv_endian(num, endian),
                         '01 B6 9B 4B E0 52 FA B1',
                         msg='Does not pass (num={})'.format(num))

    # convert a large negative int to big endian
    def test208(self):
        num = -77777779999999990000000000
        endian = 'big'
        self.assertEqual(task.conv_endian(num, endian),
                         '-40 56 15 E7 00 BC 69 D1 44 1C 00',
                         msg='Does not pass (num={})'.format(num))

    # convert an int to big endian with many trailing zeroes
    def test209(self):
        num = 2722172586950656
        endian = 'big'
        self.assertEqual(task.conv_endian(num, endian), '09 AB CD 32 10 00 00',
                         msg='Does not pass (num={})'.format(num))

    # convert an int to big endian with an initial zero
    def test210(self):
        num = 708341
        endian = 'big'
        self.assertEqual(task.conv_endian(num, endian), '0A CE F5',
                         msg='Does not pass (num={})'.format(num))

    # convert an int to big endian that has 1 byte
    def test211(self):
        num = 255
        endian = 'big'
        self.assertEqual(task.conv_endian(num, endian), 'FF',
                         msg='Does not pass (num={})'.format(num))

    # convert an int to big endian that has 2 bytes
    def test212(self):
        num = 64528
        endian = 'big'
        self.assertEqual(task.conv_endian(num, endian), 'FC 10',
                         msg='Does not pass (num={})'.format(num))

    # convert an int to big endian that has 3 bytes
    def test213(self):
        num = 16515241
        endian = 'big'
        self.assertEqual(task.conv_endian(num, endian), 'FC 00 A9',
                         msg='Does not pass (num={})'.format(num))

    # convert an int to big endian that has 4 bytes
    def test214(self):
        num = 2583429120
        endian = 'big'
        self.assertEqual(task.conv_endian(num, endian), '99 FC 00 00',
                         msg='Does not pass (num={})'.format(num))

    # convert an int to big endian that has 5 bytes
    def test215(self):
        num = 661357859293
        endian = 'big'
        self.assertEqual(task.conv_endian(num, endian), '99 FC 00 11 DD',
                         msg='Does not pass (num={})'.format(num))

    # -------------------------------------------------------------------------
    # Tests for Conversion to Little Endian
    # -------------------------------------------------------------------------
    # convert zero to little endian
    def test216(self):
        num = 0
        endian = 'little'
        self.assertEqual(task.conv_endian(num, endian), '00',
                         msg='Does not pass (num={})'.format(num))

    # convert a positive int to little endian
    def test217(self):
        num = 954786
        endian = 'little'
        self.assertEqual(task.conv_endian(num, endian), 'A2 91 0E',
                         msg='Does not pass (num={})'.format(num))

    # convert a negative int to little endian
    def test218(self):
        num = -954786
        endian = 'little'
        self.assertEqual(task.conv_endian(num, endian), '-A2 91 0E',
                         msg='Does not pass (num={})'.format(num))

    # convert a positive int to little endian with named arguments
    def test219(self):
        num = 954786
        self.assertEqual(task.conv_endian(num=954786, endian='little'),
                         'A2 91 0E',
                         msg='Does not pass (num={})'.format(num))

    # convert a negative int to little endian with named arguments
    def test220(self):
        num = -954786
        self.assertEqual(task.conv_endian(num=-954786, endian='little'),
                         '-A2 91 0E',
                         msg='Does not pass (num={})'.format(num))

    # convert a small positive int to little endian
    def test221(self):
        num = 6
        endian = 'little'
        self.assertEqual(task.conv_endian(num, endian), '06',
                         msg='Does not pass (num={})'.format(num))

    # convert a small negative int to little endian
    def test222(self):
        num = -6
        endian = 'little'
        self.assertEqual(task.conv_endian(num, endian), '-06',
                         msg='Does not pass (num={})'.format(num))

    # convert a large positive int to little endian
    def test223(self):
        num = 123456789987654321
        endian = 'little'
        self.assertEqual(task.conv_endian(num, endian),
                         'B1 FA 52 E0 4B 9B B6 01',
                         msg='Does not pass (num={})'.format(num))

    # convert a large negative int to little endian
    def test224(self):
        num = -77777779999999990000000000
        endian = 'little'
        self.assertEqual(task.conv_endian(num, endian),
                         '-00 1C 44 D1 69 BC 00 E7 15 56 40',
                         msg='Does not pass (num={})'.format(num))

    # convert an int to little endian with many trailing zeroes
    def test225(self):
        num = 2722172586950656
        endian = 'little'
        self.assertEqual(task.conv_endian(num, endian), '00 00 10 32 CD AB 09',
                         msg='Does not pass (num={})'.format(num))

    # convert an int to little endian with an initial zero
    def test226(self):
        num = 708341
        endian = 'little'
        self.assertEqual(task.conv_endian(num, endian), 'F5 CE 0A',
                         msg='Does not pass (num={})'.format(num))

    # convert an int to little endian that has 1 byte
    def test227(self):
        num = 255
        endian = 'little'
        self.assertEqual(task.conv_endian(num, endian), 'FF',
                         msg='Does not pass (num={})'.format(num))

    # convert an int to little endian that has 2 bytes
    def test228(self):
        num = 64528
        endian = 'little'
        self.assertEqual(task.conv_endian(num, endian), '10 FC',
                         msg='Does not pass (num={})'.format(num))

    # convert an int to little endian that has 3 bytes
    def test229(self):
        num = 16515241
        endian = 'little'
        self.assertEqual(task.conv_endian(num, endian), 'A9 00 FC',
                         msg='Does not pass (num={})'.format(num))

    # convert an int to little endian that has 4 bytes
    def test230(self):
        num = 2583429120
        endian = 'little'
        self.assertEqual(task.conv_endian(num, endian), '00 00 FC 99',
                         msg='Does not pass (num={})'.format(num))

    # convert an int to little endian that has 5 bytes
    def test231(self):
        num = 661357859293
        endian = 'little'
        self.assertEqual(task.conv_endian(num, endian), 'DD 11 00 FC 99',
                         msg='Does not pass (num={})'.format(num))

    # -------------------------------------------------------------------------
    # Tests for Conversion to Other Types of Endian
    # -------------------------------------------------------------------------
    # convert a positive int to small endian (which doesn't exist)
    def test232(self):
        num = 954786
        endian = 'small'
        self.assertEqual(task.conv_endian(num, endian), None,
                         msg='Does not pass (num={})'.format(num))

    # convert a negative int to small endian (which doesn't exist)
    def test233(self):
        num = -954786
        endian = 'small'
        self.assertEqual(task.conv_endian(num, endian), None,
                         msg='Does not pass (num={})'.format(num))

    # convert a positive int to biggest endian (which doesn't exist)
    def test234(self):
        num = 954786
        endian = 'biggest'
        self.assertEqual(task.conv_endian(num, endian), None,
                         msg='Does not pass (num={})'.format(num))

    # convert a negative int to littlebig endian (which doesn't exist)
    def test235(self):
        num = -954786
        endian = 'littlebig'
        self.assertEqual(task.conv_endian(num, endian), None,
                         msg='Does not pass (num={})'.format(num))

    # convert a negative int to '' endian (which doesn't exist)
    def test236(self):
        num = -954786
        endian = ''
        self.assertEqual(task.conv_endian(num, endian), None,
                         msg='Does not pass (num={})'.format(num))


if __name__ == '__main__':
    unittest.main(verbosity=2)
