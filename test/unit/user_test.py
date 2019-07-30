from test import TestCase
from src.data.repo.user import UserRepo


class GetUser(TestCase):
    def test_success(self):
        pass


class CreateUser(TestCase):
    def test_success(self):
        data = {
            "first_name": "Neil",
            "last_name": "Chudleigh",
            "email": "nchudleigh@gmail.com",
        }

