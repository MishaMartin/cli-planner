from abc import ABCMeta, abstractmethod, ABC
from collections.abc import Iterable

class DeadlinedMetaReminder(ABCMeta, Iterable):
    @abstractmethod
    def is_due(self):
        pass
class DeadlinedReminder(ABC, Iterable):
    @abstractmethod
    def is_due(self):
        pass