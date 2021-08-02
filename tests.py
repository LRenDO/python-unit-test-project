import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

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

    # Tests type for float
    def test_conv_num_hex_type(self):
        test_case = '-0xf52C'
        expected = type(-2772)
        self.assertEqual(type(task.conv_num(test_case)), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # -------------------------------------------------------------------------
    # Tests for Hex Conversion to Base 10 Integer
    # -------------------------------------------------------------------------
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

    # Tests more than one decimal point
    def test_conv_num_decimal(self):
        test_case = '.234.'
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
    def test_conv_num_prefix(self):
        test_case = '-0x'
        expected = None
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))


if __name__ == '__main__':
    unittest.main()
