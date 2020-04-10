from calculation.sum_class import Summation
import unittest


class TestsSummation(unittest.TestCase):

    def setUp(self):
        self.summation = Summation(2, 10)

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


if __name__ == "__main__":
    unittest.main()
