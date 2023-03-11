"""proposition class"""

from ast import literal_eval


class PropositionCls:
    """Class to represent a proposition with its truth table"""

    prop_exp = str
    table: list[list[str]]
    prop_type = str

    def __init__(self, prop_exp: str):
        """Initialize the proposition expression"""
        self.prop_exp = prop_exp

    def set_truth_table(self, truth_table_rows):
        """Set the truth table value"""
        if isinstance(truth_table_rows, str):
            self.table = literal_eval(truth_table_rows)
        else:
            self.table = truth_table_rows
