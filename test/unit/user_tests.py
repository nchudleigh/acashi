from test.base import TestCase
from src.domain.case.user import GetUserUseCase, CreateUserUseCase
from src.data.user import UserRepo


class GetUser(TestCase):
    def test_success(self):
        use_case = GetUserUseCase(UserRepo)
        response = use_case.go("user_x")
        user = response.data

        self.assertEqual(user.key, "user_x")
        self.assertEqual(user.first_name, "Neil")
        self.assertEqual(user.last_name, "Chudleigh")


class CreateUser(TestCase):
    def test_success(self):
        use_case = CreateUserUseCase(UserRepo)

        data = {
            "first_name": "Neil",
            "last_name": "Chudleigh",
            "email": "nchudleigh@gmail.com",
        }

        response = use_case.go(data)
        user = response.data

        self.assertIsNotNone(user.key)
        self.assertEqual(user.first_name, "Neil")
        self.assertEqual(user.last_name, "Chudleigh")
