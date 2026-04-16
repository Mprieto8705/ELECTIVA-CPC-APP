import bcrypt
from domain.ports.hash_service import HashService

class BcryptService(HashService):

    def hash(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def verify(self, password, hashed):
        return bcrypt.checkpw(password.encode(), hashed)
