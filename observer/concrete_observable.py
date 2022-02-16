from i_observable import IWeatherStation


class ConcreteStation(IWeatherStation):

    def __init__(self):
        self._temperature = None
        self._observers = []

    def __str__(self) -> str:
        return f"{self.temperature} , {self._observers}"

     
    @property
    def temperature(self):
        return self._temperature


    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.notify()

    def getState(self):
        return self._temperature

    def add(self, observer):
        self._observers.append(observer)

    def remove(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for o in self._observers:
            o.update()