from flask import Flask
from adapters.web.routes import create_routes

from infrastructure.db.sqlite_user_repository import SQLiteUserRepository
from infrastructure.security.bcrypt_service import BcryptService
from application.services.auth_service import AuthService

app = Flask(__name__)
app.secret_key = "super_secret_key"

user_repo = SQLiteUserRepository()
hash_service = BcryptService()
auth_service = AuthService(user_repo, hash_service)

app.register_blueprint(create_routes(auth_service))

if __name__ == '__main__':
    app.run(debug=True)
