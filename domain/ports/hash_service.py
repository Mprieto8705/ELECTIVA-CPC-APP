from abc import ABC, abstractmethod

class HashService(ABC):

    @abstractmethod
    def hash(self, password):
        pass

    @abstractmethod
    def verify(self, password, hashed):
        pass
