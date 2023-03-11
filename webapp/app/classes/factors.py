"""factors class"""

from ast import literal_eval


class FactorsCls:
    """Class to represent a number with its factors"""

    number = 0
    factors: list[int]
    prime_factors: list[int]

    def __init__(self, number: int):
        """Initialize the factors number"""
        self.number = number

    def __str__(self):
        """String representation for the class"""
        return f"{str(self.number)}\n{self.factors}\n{self.prime_factors}"

    def set_factors(self, factors):
        if isinstance(factors, str):
            self.factors = literal_eval(factors)
        else:
            self.factors = factors

    def set_prime_factors(self, prime_factors):
        if isinstance(prime_factors, str):
            self.prime_factors = literal_eval(prime_factors)
        else:
            self.prime_factors = prime_factors
