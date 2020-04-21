from calculation.subtraction import Subtraction
from calculation.summation import Summation
from game import Game

import unittest


class GameClass(unittest.TestCase):

    def test_get_calculation_class_should_return_all_classes(self):
        expected_class_names = [Subtraction.__name__, Summation.__name__]

        for i in range(100):
            result = Game.get_calculation_class()
            class_name = result.__class__.__name__
            if class_name in expected_class_names:
                expected_class_names.remove(class_name)

            if len(expected_class_names) == 0:
                break

        self.assertEmpty(expected_class_names)

    def assertEmpty(self, list_classes):
        if len(list_classes) != 0:
            self.fail("The list is expected to be empty but it was not.")


if __name__ == "__main__":
    unittest.main()
