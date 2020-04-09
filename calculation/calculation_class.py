from abc import ABC, abstractmethod


class Calculation(ABC):
    def __init__(self, term_min: int, term_max: int):
        pass

    @abstractmethod
    def get_calculation(self):
        pass
