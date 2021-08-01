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


if __name__ == '__main__':
    unittest.main()
