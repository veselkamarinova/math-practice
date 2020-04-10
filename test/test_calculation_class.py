from calculation.calculation_class import Calculation
from calculation.summation import Summation

import unittest


class TestsCalculationClass(unittest.TestCase):

    def test_class_can_be_instantiated_using_correct_values(self):
        expected_min = 1
        expected_max = 10
        sum = Summation(expected_min, expected_max)
        actual_min = sum.term_min
        actual_max = sum.term_max
        self.assertEqual(actual_min, expected_min)
        self.assertEqual(actual_max, expected_max)

    def test_that_negative_term_min_raises_error(self):
        with self.assertRaises(ValueError) as cm:
            Summation(-1, 10)
        self.assertEqual(str(cm.exception), "Only positive integers are allowed.")

    def test_that_negative_term_max_raises_error(self):
        with self.assertRaises(ValueError) as cm:
            Summation(1, -1)
        self.assertEqual(str(cm.exception), "Only positive integers are allowed.")

    def test_that_term_max_lower_than_tem_min_raises_error(self):
        with self.assertRaises(ValueError) as cm:
            Summation(4, 1)
        self.assertEqual(str(cm.exception), "term_max must be larger than term_min")

    def test_term_max_is_equal_to_term_min_raises_error(self):
        with self.assertRaises(ValueError) as cm:
            Summation(4, 4)
        self.assertEqual(str(cm.exception), "term_max must be larger than term_min")

    def test_that_invalid_types_as_string_raises_error(self):
        with self.assertRaises(Exception) as cm:
            Summation(1, "five")
        self.assertTrue(str(cm.exception), "Only positive integers are allowed.")

    def test_that_invalid_types_as_string_raises_error_using_term_min(self):
        with self.assertRaises(Exception) as cm:
            Summation("five", 5)
        self.assertTrue(str(cm.exception), "Only positive integers are allowed.")

    def test_that_invalid_types_as_float_number_raises_error(self):
        with self.assertRaises(TypeError) as cm:
            Summation(1, 5.5)
        self.assertTrue(str(cm.exception), "Only positive integers are allowed.")

    def test_that_invalid_types_as_float_number_raises_error_using_term_min(self):
        with self.assertRaises(TypeError) as cm:
            Summation(5.5, 6)
        self.assertTrue(str(cm.exception), "Only positive integers are allowed.")


if __name__ == "__main__":
    unittest.main()
