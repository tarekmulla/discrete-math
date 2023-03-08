'''question class'''


class QuestionCls:
    '''Class to represent a question'''
    question = ""

    def __init__(self, question: str):
        '''Initialize the question parameters'''
        self.question = question

    def __str__(self):
        '''String representation for the class'''
        return self.question

    @classmethod
    # pylint: disable=bad-staticmethod-argument
    def load(cls, question_dict: dict):
        '''Load question from dictionary'''
        question_obj = object.__new__(cls)
        question_obj.question = question_dict['question']
        return question_obj
