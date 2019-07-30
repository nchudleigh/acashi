from test import TestCase
from src.data.repo.user import UserRepo
from src.domain.entity.user import UserEntity


class GetUser(TestCase):
    def test_success(self):
        pass


# What do we need this for
# class CreateUser(TestCase):
def test_whenValid_userCreated():
    user_ent = UserEntity(name="Neil", key="user_xxx", created_at=3213213)

    result = UserRepo().create(user_ent)
    assert result.name == "Neil"
    assert result.key == "user_xxx"
    assert result.created_at == 3213213

