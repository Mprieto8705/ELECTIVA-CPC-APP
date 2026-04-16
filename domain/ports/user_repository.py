from abc import ABC, abstractmethod

class UserRepository(ABC):

    @abstractmethod
    def save(self, user):
        pass

    @abstractmethod
    def find_by_username(self, username):
        pass
