from abc import abstractmethod, ABCMeta


class IObserver(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass
