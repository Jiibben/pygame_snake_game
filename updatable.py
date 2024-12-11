from abc import ABC,abstractmethod

class Updatable(ABC):
    @abstractmethod
    def update(self):
        """update it on each tick"""