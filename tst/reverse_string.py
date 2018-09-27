import unittest

from src.reverse_string import reverse_string_while_loop, reverse_string_for_loop, reverse_string_recursion_1, \
    reverse_string_recursion_2


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
        self.assertEqual(self.expected_even, reversed_s)

    def test_reverse_while_loop_odd(self):
        # Action
        reversed_s = reverse_string_while_loop(self.string_odd)

        # Assert
        self.assertEqual(self.expected_odd, reversed_s)

    def test_reverse_for_loop_even(self):
        # Action
        reversed_s = reverse_string_for_loop(self.string_even)

        # Assert
        self.assertEqual(self.expected_even, reversed_s)

    def test_reverse_for_loop_odd(self):
        # Action
        reversed_s = reverse_string_for_loop(self.string_odd)

        # Assert
        self.assertEqual(self.expected_odd, reversed_s)

    def test_reverse_recursion_1_even(self):
        # Action
        reversed_s = reverse_string_recursion_1(self.string_even)

        # Assert
        self.assertEqual(self.expected_even, reversed_s)

    def test_reverse_recursion_1_odd(self):
        # Action
        reversed_s = reverse_string_recursion_1(self.string_odd)

        # Assert
        self.assertEqual(self.expected_odd, reversed_s)

    def test_reverse_recursion_2_even(self):
        # Action
        reversed_s = reverse_string_recursion_2(self.string_even)

        # Assert
        self.assertEqual(self.expected_even, reversed_s)

    def test_reverse_recursion_2_odd(self):
        # Action
        reversed_s = reverse_string_recursion_2(self.string_odd)

        # Assert
        self.assertEqual(self.expected_odd, reversed_s)
