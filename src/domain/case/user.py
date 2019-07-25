from src.domain.case import Case
from src.domain.model.user import User

from time import time
from uuid import uuid4

"""
Use cases encapsulate core domain logic.
"""


class GetUserUseCase(Case):
    def go(self, key: str):
        user_dto = self.UserRepo.get_by_key(key)
        return user_dto


class GetUserByEmailUseCase(Case):
    def go(self, email: str):
        user_dto = self.UserRepo.get_by_email(email)
        return user_dto


class CreateUserUseCase(Case):
    def go(self, data: dict):

        generated_key = uuid4().hex
        user_key = f"user_{generated_key}"

        # NOTE: `key` and `created_at` could easily be abstracted into our Model Base class
        # They are so common in our codebase I think this would be a reasonable gain
        new_user = User(key=user_key, created_at=int(time()), **data)

        user_repo = self.UserRepo()

        user_repo.create(new_user)

        return new_user


class UpdateUserUseCase(Case):
    def go(self, data: dict):
        # check required variables are set
        if (
            data.get("first_name") is None
            and data.get("last_name") is None
            and data.get("email") is None
        ):
            # TODO: error response
            return

        user_dto = self.UserRepo.update(data)

        return user_dto


class DeleteUserUseCase(Case):
    def go(self, key: str):
        user = self.UserRepo.delete_by_key(key)
