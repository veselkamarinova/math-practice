from calculation.calculation_class import Calculation


class Summation(Calculation):
    def get_calculation(self):
        term1 = self.get_random_term()
        term2 = self.get_random_term()
        calculation = str(term1) + " + " + str(term2)
        result = term1 + term2
        return calculation, result
