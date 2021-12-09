from abc import ABCMeta, abstractmethod, ABC
from collections.abc import Iterable
from dateutil.parser import parse

class DeadlinedMetaReminder(ABCMeta, Iterable):
    @abstractmethod
    def is_due(self):
        pass
class DateLinedReminder(ABC, Iterable):
    @abstractmethod
    def is_due(self):
        pass

class DateReminder(DateLinedReminder):
    def __init__(self, text, date):
        self.parse(date) 
        dayfirst=True