from main import *

from unittest import TestCase

class TestMain(TestCase):

    def test__prime_true1(self):
        expected = True
        result = prime_check(13)
        self.assertEqual(expected, result)

    def test__prime_true2(self):
        expected = True
        result = prime_check(1)
        self.assertEqual(expected, result)

    def test__prime_true3(self):
        expected = True
        result = prime_check(2)
        self.assertEqual(expected, result)

    def test__prime_false(self):
        expected = False
        result = prime_check(16)
        self.assertEqual(expected, result)

    def test__prime_false2(self):
        expected = False
        result = prime_check(9)
        self.assertEqual(expected, result)

    def test__square_check_true1(self):
        expected = True
        result = square_number_check(9)
        self.assertEqual(expected, result)

    def test__square_check_true2(self):
        expected = True
        result = square_number_check(4)
        self.assertEqual(expected, result)

    def test__square_check_false1(self):
        expected = False
        result = square_number_check(8)
        self.assertEqual(expected, result)

    def test__square_check_false2(self):
        expected = False
        result = square_number_check(2)
        self.assertEqual(expected, result)

    def test__main_is_callable(self):
        main()
