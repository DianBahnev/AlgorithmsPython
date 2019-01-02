import unittest

from src.sorting.merge_sort import merge, merge_sort, merge_in_place, merge_sort_in_place


class Merge(unittest.TestCase):

    def test_arrays_1_1(self):
        # Given
        l1 = [2]
        l2 = [1]
        expectd = [1, 2]

        # When
        merged_l = merge(l1, l2)

        # Then
        self.assertEqual(merged_l, expectd)

    def test_arrays_2_1(self):
        # Given
        l1 = [2, 3]
        l2 = [1]
        expectd = [1, 2, 3]

        # When
        merged_l = merge(l1, l2)

        # Then
        self.assertEqual(merged_l, expectd)

    def test_arrays_2_2(self):
        # Given
        l1 = [6, 9]
        l2 = [3, 8]
        expectd = [3, 6, 8, 9]

        # When
        merged_l = merge(l1, l2)

        # Then
        self.assertEqual(merged_l, expectd)


class MergeSort(unittest.TestCase):

    def test_1(self):
        # Given
        ls = [1]
        expected = [1]

        # When
        sorted_l = merge_sort(ls)

        # Then
        self.assertEqual(sorted_l, expected)

    def test_2(self):
        # Given
        ls = [2, 1]
        expected = [1, 2]

        # When
        sorted_l = merge_sort(ls)

        # Then
        self.assertEqual(sorted_l, expected)

    def test_3(self):
        # Given
        ls = [2, 1, 3]
        expected = [1, 2, 3]

        # When
        sorted_l = merge_sort(ls)

        # Then
        self.assertEqual(sorted_l, expected)

    def test_4(self):
        # Given
        ls = [2, 1, 8, 3]
        expected = [1, 2, 3, 8]

        # When
        sorted_l = merge_sort(ls)

        # Then
        self.assertEqual(sorted_l, expected)

    def test_5(self):
        # Given
        ls = [2, 1, 8, 3, 0]
        expected = [0, 1, 2, 3, 8]

        # When
        sorted_l = merge_sort(ls)

        # Then
        self.assertEqual(sorted_l, expected)

    def test_6(self):
        # Given
        ls = [2, 1, 8, 3, 0, 8, 5, 1, 7, 2]
        expected = [0, 1, 1, 2, 2, 3, 5, 7, 8, 8]

        # When
        sorted_l = merge_sort(ls)

        # Then
        self.assertEqual(sorted_l, expected)


class MergeInPlace(unittest.TestCase):

    def test_1(self):
        # Given
        ls = [1, 1]
        expected = [1, 1]

        # When
        merge_in_place(ls, 0, 1, len(ls))

        # Then
        self.assertEqual(ls, expected)

    def test_2(self):
        # Given
        ls = [2, 1]
        expected = [1, 2]

        # When
        merge_in_place(ls, 0, 1, len(ls))

        # Then
        self.assertEqual(ls, expected)

    def test_3(self):
        # Given
        ls = [2, 1, 3]
        expected = [1, 2, 3]

        # When
        merge_in_place(ls, 0, 1, len(ls))

        # Then
        self.assertEqual(ls, expected)

    def test_4(self):
        # Given
        ls = [1, 3, 2]
        expected = [1, 2, 3]

        # When
        merge_in_place(ls, 0, 2, len(ls))

        # Then
        self.assertEqual(ls, expected)

    def test_5(self):
        # Given
        ls = [1, 3, 2, 5]
        expected = [1, 2, 3, 5]

        # When
        merge_in_place(ls, 0, 2, len(ls))

        # Then
        self.assertEqual(ls, expected)


class MergeSortInPlace(unittest.TestCase):

    def test_1(self):
        # Given
        ls = [1]
        expected = [1]

        # When
        merge_sort_in_place(ls, 0, len(ls) -1)

        # then
        self.assertEqual(ls, expected)

    def test_2(self):
        # Given
        ls = [1, 2]
        expected = [1, 2]

        # When
        merge_sort_in_place(ls, 0, len(ls))

        # then
        self.assertEqual(ls, expected)

    def test_3(self):
        # Given
        ls = [2, 1]
        expected = [1, 2]

        # When
        merge_sort_in_place(ls, 0, len(ls))

        # then
        self.assertEqual(ls, expected)

    def test_3(self):
        # Given
        ls = [2, 1, 3]
        expected = [1, 2, 3]

        # When
        merge_sort_in_place(ls, 0, len(ls))

        # then
        self.assertEqual(ls, expected)

    def test_4(self):
        # Given
        ls = [2, 9, 1, 3, 4, 0]
        expected = [0, 1, 2, 3, 4, 9]

        # When
        merge_sort_in_place(ls, 0, len(ls))

        # then
        self.assertEqual(ls, expected)

    def test_5(self):
        # Given
        ls = [11, 2, 9, 1, 12, 3, 4, 0, 19]
        expected = [0, 1, 2, 3, 4, 9, 11, 12, 19]

        # When
        merge_sort_in_place(ls, 0, len(ls))

        # then
        self.assertEqual(ls, expected)

