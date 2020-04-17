from calculation.subtraction import Subtraction
import unittest


class TestsSubtraction(unittest.TestCase):

    def setUp(self):
        self.subtraction = Subtraction(2, 10)

    def test_get_random_term(self):
        lowest = None
        highest = None

        for i in range(1000):
            random_term = self.subtraction.get_random_term()
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
        for i in range(100):
            calculation = self.subtraction.get_calculation()

            # Check that a tuple is returned with the first value a string and the second an integer.
            self.assertTrue(isinstance(calculation, tuple))
            sub = calculation[0]
            result = calculation[1]
            self.assertTrue(isinstance(sub, str))
            self.assertTrue(isinstance(result, int))

            # Check that the sub and the result are correct.
            sub_result = eval(sub)
            self.assertEqual(result, sub_result)


if __name__ == "__main__":
    unittest.main()
