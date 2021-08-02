import unittest
from task import conv_endian


class TestCase(unittest.TestCase):
    # Function 1 Tests

    # Function 2 Tests

    # Function 3 Tests
    # convert a positive int to big endian
    def test201(self):
        num = 954786
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), '0E 91 A2',
                         msg='Does not pass (num={})'.format(num))

    # convert a positive int with the endian argument omitted
    def test202(self):
        num = 954786
        self.assertEqual(conv_endian(num), '0E 91 A2',
                         msg='Does not pass (num={})'.format(num))

    # convert a negative int to big endian
    def test203(self):
        num = -954786
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), '-0E 91 A2',
                         msg='Does not pass (num={})'.format(num))

    # convert a positive int to little endian
    def test204(self):
        num = 954786
        endian = 'little'
        self.assertEqual(conv_endian(num, endian), 'A2 91 0E',
                         msg='Does not pass (num={})'.format(num))

    # convert a negative int to little endian
    def test205(self):
        num = -954786
        endian = 'little'
        self.assertEqual(conv_endian(num, endian), '-A2 91 0E',
                         msg='Does not pass (num={})'.format(num))

    # convert a positive int to little endian with named arguments
    def test206(self):
        num = 954786
        self.assertEqual(conv_endian(num=954786, endian='little'), 'A2 91 0E',
                         msg='Does not pass (num={})'.format(num))

    # convert a negative int to little endian with named arguments
    def test207(self):
        num = -954786
        self.assertEqual(conv_endian(num=-954786, endian='little'),
                         '-A2 91 0E',
                         msg='Does not pass (num={})'.format(num))

    # convert a positive int to small endian (which doesn't exist)
    def test208(self):
        num = 954786
        endian = 'small'
        self.assertEqual(conv_endian(num, endian), None,
                         msg='Does not pass (num={})'.format(num))

    # convert a negative int to small endian (which doesn't exist)
    def test209(self):
        num = -954786
        endian = 'small'
        self.assertEqual(conv_endian(num, endian), None,
                         msg='Does not pass (num={})'.format(num))

    # convert a small positive int to big endian
    def test210(self):
        num = 6
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), '06',
                         msg='Does not pass (num={})'.format(num))

    # convert a small negative int to big endian
    def test211(self):
        num = -6
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), '-06',
                         msg='Does not pass (num={})'.format(num))

    # convert a small positive int to little endian
    def test212(self):
        num = 6
        endian = 'little'
        self.assertEqual(conv_endian(num, endian), '06',
                         msg='Does not pass (num={})'.format(num))

    # convert a small negative int to little endian
    def test213(self):
        num = -6
        endian = 'little'
        self.assertEqual(conv_endian(num, endian), '-06',
                         msg='Does not pass (num={})'.format(num))


if __name__ == '__main__':
    unittest.main(verbosity=2)
