from test import TestCase
from src.library.crypt_keeper import CryptKeeper


DEFAULT_PASSWORD = "howsyourknee"
DEFAULT_ITERATIONS = 10


class HashPassword(TestCase):
    def hash_password(self, password=DEFAULT_PASSWORD):
        ck = CryptKeeper(iterations=DEFAULT_ITERATIONS)
        return ck.hash_password(password)

    def test_random(self):
        """Same password hashed again does not produce the same result"""

        hashed_password, salt = self.hash_password(DEFAULT_PASSWORD)
        hashed_password2, salt2 = self.hash_password(DEFAULT_PASSWORD)
        hashed_password3, salt3 = self.hash_password(DEFAULT_PASSWORD)

        self.assertTrue(hashed_password != hashed_password2)
        self.assertTrue(hashed_password != hashed_password3)
        self.assertTrue(hashed_password2 != hashed_password3)

        self.assertTrue(salt != salt2)
        self.assertTrue(salt != salt3)
        self.assertTrue(salt2 != salt3)

    def test_length(self, minimum_length=20):
        f"""Result is at least {minimum_length} characters long"""
        hashed_password, salt = self.hash_password(DEFAULT_PASSWORD)
        self.assertTrue(len(hashed_password) > minimum_length)

    def test_type(self):
        """Hased password and salt are strings"""
        hashed_password, salt = self.hash_password()
        self.assertTrue(type(hashed_password) == str)
        self.assertTrue(type(salt) == str)


class CheckPassword(TestCase):
    def check_password(self, password, salt, hashed_password, iterations=None):
        if iterations:
            ck = CryptKeeper(iterations=iterations)
        else:
            ck = CryptKeeper(iterations=DEFAULT_ITERATIONS)

        return ck.check_password(password, salt, hashed_password)

    def hash_password(self, password=DEFAULT_PASSWORD):
        ck = CryptKeeper(iterations=DEFAULT_ITERATIONS)
        return ck.hash_password(password)

    def test_iterations(self):
        """Number of iterations affects check"""
        hashed_password, salt = self.hash_password()

        self.assertTrue(self.check_password(DEFAULT_PASSWORD, salt, hashed_password))
        self.assertFalse(
            self.check_password(DEFAULT_PASSWORD, salt, hashed_password, iterations=20)
        )

    def test_salt(self):
        """Salt affects check"""
        hashed_password, correct_salt = self.hash_password()
        wrong_salt = "himilayan"

        self.assertTrue(
            self.check_password(DEFAULT_PASSWORD, correct_salt, hashed_password)
        )
        self.assertFalse(
            self.check_password(DEFAULT_PASSWORD, wrong_salt, hashed_password)
        )

    def test_password(self):
        """Password affects check"""
        hashed_password, salt = self.hash_password()

        self.assertTrue(self.check_password(DEFAULT_PASSWORD, salt, hashed_password))
        self.assertTrue(
            self.check_password("thatsallicareabout", salt, hashed_password) == False
        )
