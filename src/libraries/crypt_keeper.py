import pbkdf2
import uuid


class CryptKeeper:
    def __init__(self, iterations=50000):
        self.iterations = iterations

    def _crypt(self, password, salt):
        return pbkdf2.crypt(password, salt, self.iterations)

    def _create_salt(self):
        return uuid.uuid4().hex

    def hash_password(self, password):
        salt = self._create_salt()
        hashed_password = self._crypt(password, salt)
        return hashed_password, salt

    def check_password(self, password_attempt, salt, hashed_password):
        hashed_password_attempt = self._crypt(password_attempt, salt)
        is_valid = hashed_password == hashed_password_attempt
        return is_valid
