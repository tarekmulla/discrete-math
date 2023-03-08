from enum import Enum


class Alert:
    '''Class to create alerts that show to the user'''
    class Category(Enum):
        '''Enumeration for alert types'''
        ERROR = 'danger'
        WARNING = 'warning'
        SUCCESS = 'success'
        INFO = 'info'

    def __init__(self, message, category: Category):
        self.message = message
        self.category = category
