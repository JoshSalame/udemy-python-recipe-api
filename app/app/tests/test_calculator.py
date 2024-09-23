from django.test import SimpleTestCase

from app import calculator

class CalculatorTest(SimpleTestCase):

    def test_add(self):
        x = 5
        y = 7

        result = calculator.add(x, y)

        self.assertEqual(result, 12)

    def test_subtract(self):
        x = 42
        y = 6

        result = calculator.subtract(x, y)

        self.assertEqual(result, 36)
