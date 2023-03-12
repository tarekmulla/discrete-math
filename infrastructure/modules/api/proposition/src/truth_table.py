"""generate truth table for a proposition
credit to: https://github.com/xehoth/TruthTableGenerator"""

from enum import Enum
from typing import List
import re


class PropType(Enum):
    '''represnt the proposition type'''
    TAUTOLOGY = "Tautology"
    CONTRADICTION = "Contradiction"
    CONTINGENCY = "Contingency"


class Proposition:
    '''evaluate proposition'''
    def __init__(self, value=False):
        self.value = value

    def __rshift__(self, rhs):  # ->
        return Proposition(not (self.value and not rhs.value))

    def __add__(self, rhs):  # or
        return Proposition(self.value or rhs.value)

    def __mul__(self, rhs):  # and
        return Proposition(self.value and rhs.value)

    def __invert__(self):  # not
        return Proposition(not self.value)

    def __eq__(self, rhs):  # <->
        return Proposition((self.value and rhs.value) or (not self.value and not rhs.value))

    def __ne__(self, rhs):  # ^
        return Proposition(self.value != rhs.value)


def getPropositions(s: str) -> List[str]:
    '''get list of propositions'''
    return list(sorted(set(re.findall(r'\w+', s.replace("T", "").replace("F", "")))))


def getEvalExpression(s: str):
    '''format the proposition by unified the symbols'''
    # not
    s = s.replace("!", "~").replace("not", "~").replace(
        "¬", "~").replace(r"\neg", "~").replace(r"∼", "~")
    # and
    s = s.replace("&", "*").replace(r"\wedge", "*").replace("and",
                                                            "*").replace("∧", "*")
    # or
    s = s.replace("|", "+").replace(r"\vee", "+").replace("or",
                                                          "+").replace("∨", "+").replace("v", "+")
    # <->
    s = s.replace("<->", "==").replace("↔", "==").replace(r"\leftrightarrow",
                                                          "==").replace(r"⇔", "==").replace("<=>", "==")
    # ->
    s = s.replace("->", ">>").replace("→", ">>").replace(r"\rightarrow", ">>").replace("⇒", ">>")
    # ^
    s = s.replace("^", "!=").replace("⊕", "!=")
    return s


def generate_truth_table(expression: str, reverse=True) -> None:
    # True
    T = Proposition(True)
    # False
    F = Proposition(False)
    # strip
    expression = expression.strip()
    # eval string
    s = getEvalExpression(expression)

    # tautology & contradictions
    tautology = True
    contradictions = False

    props = getPropositions(s)
    n = len(props)
    # prop eval buffer
    buf = [Proposition() for i in range(n)] + [T, F]

    table_rows = [[]]
    # append the header
    for i in props + [expression]:
        table_rows[0].append(i)

    states = range(0, 1 << n)

    for state in reversed(states) if reverse else states:
        row = []
        for i in range(n):
            buf[i].value = (state >> (n - i - 1)) & 1 == 1
            row.append("FT"[buf[i].value])
        # pylint: disable=eval-used
        res = eval("(" + s + ").value", {v: buf[i] for i, v in enumerate(props + ['T', 'F'])})
        row.append("FT"[res])
        table_rows.append(row)
        tautology = tautology and res
        contradictions = contradictions or res
    prop_type = PropType.CONTINGENCY
    if tautology:
        prop_type = PropType.TAUTOLOGY
    if not contradictions:
        prop_type = PropType.CONTRADICTION

    return table_rows, prop_type
