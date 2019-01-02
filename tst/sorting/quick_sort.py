import unittest

from src.sorting.quick_sort import quick_sort


class QuickSort(unittest.TestCase):

    def setUp(self):
        self.numbers_len_1 = [1]
        self.numbers_len_2 = [2, 1]
        self.numbers_len_3 = [2, 1, 3]
        self.numbers_len_4 = [0, 2, 1, 3]
        self.numbers_len_5 = [3, 7, 4, 12, 1]

        self.expected_numbers_len_1 = [1]
        self.expected_numbers_len_2 = [1, 2]
        self.expected_numbers_len_3 = [1, 2, 3]
        self.expected_numbers_len_4 = [0, 1, 2, 3]
        self.expected_numbers_len_5 = [1, 3, 4, 7, 12]

    def test_quick_sort_1(self):
        quick_sort(self.numbers_len_1, 0, len(self.numbers_len_1) - 1)

        self.assertEqual(self.numbers_len_1, self.expected_numbers_len_1)

    def test_quick_sort_2(self):
        quick_sort(self.numbers_len_2, 0, len(self.numbers_len_2) - 1)

        self.assertEqual(self.numbers_len_2, self.expected_numbers_len_2)

    def test_quick_sort_3(self):
        quick_sort(self.numbers_len_3, 0, len(self.numbers_len_3) - 1)

        self.assertEqual(self.numbers_len_3, self.expected_numbers_len_3)

    def test_quick_sort_4(self):
        quick_sort(self.numbers_len_4, 0, len(self.numbers_len_4) - 1)

        self.assertEqual(self.numbers_len_4, self.expected_numbers_len_4)

    def test_quick_sort_5(self):
        quick_sort(self.numbers_len_5, 0, len(self.numbers_len_5) - 1)

        self.assertEqual(self.numbers_len_5, self.expected_numbers_len_5)
