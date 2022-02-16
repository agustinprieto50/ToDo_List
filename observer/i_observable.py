from abc import abstractmethod, ABCMeta


class IWeatherStation(metaclass=ABCMeta):
    @abstractmethod
    def add(self, observer):
        pass

    @abstractmethod
    def remove(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def getState(self):
        pass