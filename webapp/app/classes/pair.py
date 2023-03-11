"""number pair class"""

from ast import literal_eval


class PairCls:
    """Class to represent 2 numbers with its GCD and LCM"""

    number1: int
    number2: int
    gcd: int
    lcm: int
    bezout_x: int
    bezout_y: int
    euclidean_steps: list[int]

    def __init__(self, number1: int, number2: int):
        """Initialize the two number"""
        self.number1 = max(number1, number2)
        self.number2 = min(number1, number2)

    def __str__(self):
        """String representation for the class"""
        return f"({str(self.number1)}, {self.number2})"

    def get_bezout_equation(self):
        """return the bezout equations as string"""
        return f"{self.gcd} = {self.bezout_x}({self.number1}) - \
            {self.bezout_y}({self.number2})"

    def set_euclidean_steps(self, euclidean_steps):
        if isinstance(euclidean_steps, str):
            self.euclidean_steps = literal_eval(euclidean_steps)
        else:
            self.euclidean_steps = euclidean_steps
