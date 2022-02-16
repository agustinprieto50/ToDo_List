from i_observer import IObserver


class ConcreteObserver(IObserver):

    def __init__(self, observable):
        self._observable = observable

    def update(self):
        state = self._observable.getState()
        print( f"Hoy hacen {state} grados" )