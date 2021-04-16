from abc import ABC, abstractmethod

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        print("Running GUI")
        pass

class Terminal(Ui):
    def __init__(self):
        pass

    def run(self):
        print("Running Terminal")
        pass
