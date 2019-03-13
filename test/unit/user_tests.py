from test.base import TestCase
from src.domain.case.user import GetUserUseCase, CreateUserUseCase
from src.data.user import UserRepo


class GetUser(TestCase):
    def test_success(self):
        r = UserRepo()
        uc = GetUserUseCase(r)
        result = uc.go("user_x")


class CreateUser(TestCase):
    def test_success(self):
        r = UserRepo()
        uc = CreateUserUseCase(r)
        result = uc.go(
            {
                "first_name": "Neil",
                "last_name": "Chudleigh",
                "email": "nchudleigh@gmail.com",
            }
        )

        self.assertIsNotNone(result.data["key"])
        self.assertEqual(result.data["first_name"], "Neil")
        self.assertEqual(result.data["last_name"], "Chudleigh")
