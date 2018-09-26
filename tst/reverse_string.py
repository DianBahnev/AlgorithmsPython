import unittest

from src.reverse_string import reverse_string_while_loop, reverse_string_for_loop


class ReverseString(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.string_odd = 'abcdefg'
        cls.string_even = 'abcdef'

        cls.expected_odd = 'gfedcba'
        cls.expected_even = 'fedcba'

    def test_reverse_while_loop_even(self):
        # Action
        reversed_s = reverse_string_while_loop(self.string_even)

        # Assert
        self.assertEqual(reversed_s, self.expected_even)

    def test_reverse_while_loop_odd(self):
        # Action
        reversed_s = reverse_string_while_loop(self.string_odd)

        # Assert
        self.assertEqual(reversed_s, self.expected_odd)

    def test_reverse_for_loop_even(self):
        # Action
        reversed_s = reverse_string_for_loop(self.string_even)

        # Assert
        self.assertEqual(reversed_s, self.expected_even)

    def test_reverse_for_loop_odd(self):
        # Action
        reversed_s = reverse_string_for_loop(self.string_odd)

        # Assert
        self.assertEqual(reversed_s, self.expected_odd)

