from abc import ABC, abstractmethod


class FeeCalculator(ABC):

    @abstractmethod
    def calculate(self, ticket):
        pass
