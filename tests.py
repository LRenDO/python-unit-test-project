import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

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

    # Tests conversion to float 0
    def test_conv_num_float_0(self):
        test_case = '0'
        expected = 0
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

    # Tests hex conversion to base 10 0x0
    def test_conv_num_hex_0(self):
        test_case = '0x0'
        expected = 0
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests hex conversion to base 10 0x0
    def test_conv_num_hex_neg0(self):
        test_case = '-0x0'
        expected = None
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests hex conversion to base 10 0xAD4
    def test_conv_num_hex_pos(self):
        test_case = '0xAD4'
        expected = 2772
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))

    # Tests hex conversion to base 10 -0xF52C
    def test_conv_num_hex_neg(self):
        test_case = '-0xF52C'
        expected = -2772
        self.assertEqual(task.conv_num(test_case), expected,
                         msg='conv_num({}) Failed'.format(expected))


if __name__ == '__main__':
    unittest.main()
