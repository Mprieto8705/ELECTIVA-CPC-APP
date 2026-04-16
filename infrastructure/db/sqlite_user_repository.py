import sqlite3
from domain.ports.user_repository import UserRepository
from domain.models.user import User

class SQLiteUserRepository(UserRepository):

    def __init__(self):
        self.conn = sqlite3.connect("users.db", check_same_thread=False)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password BLOB,
            role TEXT
        )
        """)
        self.conn.commit()

    def save(self, user):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO users VALUES (?, ?, ?)",
            (user.username, user.password, user.role)
        )
        self.conn.commit()

    def find_by_username(self, username):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        result = cursor.fetchone()

        if result:
            return User(result[0], result[1], result[2])
        return None
