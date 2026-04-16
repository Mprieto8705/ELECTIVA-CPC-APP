from domain.models.user import User

class AuthService:

    def __init__(self, user_repo, hash_service):
        self.user_repo = user_repo
        self.hash_service = hash_service

    def register(self, username, password, role):
        hashed = self.hash_service.hash(password)
        user = User(username, hashed, role)
        self.user_repo.save(user)

    def login(self, username, password):
        user = self.user_repo.find_by_username(username)

        if not user:
            return None

        if self.hash_service.verify(password, user.password):
            return user

        return None
