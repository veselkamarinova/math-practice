from calculation.summation import Summation
from calculation.calculation_class import Calculation
import unittest


class TestsSummation(unittest.TestCase):

    def setUp(self):
        self.summation = Summation(2, 10, 20)

    def test_get_random_term(self):
        lowest = None
        highest = None

        for i in range(1000):
            random_term = self.summation.get_random_term()
            self.assertNotLess(random_term, 2)
            self.assertNotGreater(random_term, 10)

            if lowest is None:
                lowest = random_term
            elif random_term < lowest:
                lowest = random_term
            if highest is None:
                highest = random_term
            elif random_term > highest:
                highest = random_term

            if lowest == 2 and highest == 10:
                break

        self.assertEqual(2, lowest)
        self.assertEqual(10, highest)

    def assertNotLess(self, a, b):
        if a < b:
            self.fail(str(a) + " can not be less than " + str(b))

    def assertNotGreater(self, a, b):
        if a > b:
            self.fail(str(a) + " can not be greater than " + str(b))

    def test_get_calculation(self):
        max_result_found = 0
        for i in range(1000):
            calculation = self.summation.get_calculation()
            # Check that a tuple is returned with the first value a string and the second an integer.
            self.assertTrue(isinstance(calculation, tuple))
            sum = calculation[0]
            result = calculation[1]
            if result > max_result_found:
                max_result_found = result
            self.assertTrue(isinstance(sum, str))
            self.assertTrue(isinstance(result, int))

            # Check that the sum and the result are correct.
            sum_result = eval(sum)
            self.assertEqual(result, sum_result)

        # Check that the result returned is never greater than the result_max.
        self.assertEqual(max_result_found, 20)


if __name__ == "__main__":
    unittest.main()
