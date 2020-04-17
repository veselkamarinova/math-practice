from calculation.calculation_class import Calculation


class Subtraction(Calculation):
    def get_calculation(self):
        term1 = self.get_random_term()
        term2 = self.get_random_term()
        if term1 >= term2:
            calculation = str(term1) + " - " + str(term2)
            result = term1 - term2
        else:
            calculation = str(term2) + " - " + str(term1)
            result = term2 - term1
        return calculation, result


