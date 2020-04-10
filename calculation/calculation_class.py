from abc import ABC, abstractmethod
import random


class Calculation(ABC):
    def __init__(self, term_min: int, term_max: int):
        self.term_min = term_min
        self.term_max = term_max
        if self.term_min < 0 or self.term_max < 0:
            raise ValueError("Only positive integers are allowed.")
        if self.term_max <= self.term_min:
            raise ValueError("term_max must be larger than term_min")
        if not isinstance(term_min, int):
            raise TypeError("Only positive integers are allowed.")
        if not isinstance(term_max, int):
            raise TypeError("Only positive integers are allowed.")

    @abstractmethod
    def get_calculation(self):
        pass

    def get_random_term(self):
        min_range = self.term_min
        max_range = self.term_max + 1
        return random.randrange(min_range, max_range)
