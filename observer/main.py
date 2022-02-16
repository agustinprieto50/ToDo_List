from os import stat
from concrete_observer import ConcreteObserver
from concrete_observable import ConcreteStation


if __name__ == "__main__":

    station = ConcreteStation()

    theWeatherChannel = ConcreteObserver(station)
    observer2 = ConcreteObserver(station)
    station.add(theWeatherChannel)
    station.add(observer2)

    station.temperature = 35
    station.temperature = 30
