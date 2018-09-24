import unittest

from src.reverse_polish_notation_translation import transform_expression


class ReversePolish(unittest.TestCase):

    def test_1(self):
        expression = '(a+b)'
        expected = 'ab+'

        converted = transform_expression(expression)
        self.assertEqual(expected, converted)

    def test_2(self):
        expression = '(a+(b*c))'
        expected = 'abc*+'

        converted = transform_expression(expression)
        self.assertEqual(expected, converted)

    def test_3(self):
        expression = '((a+t)*((b+(a+c))^(c+d)))'
        expected = 'at+bac++cd+^*'

        converted = transform_expression(expression)
        self.assertEqual(expected, converted)
