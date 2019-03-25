from src.domain.case import Case
from src.domain.model.user import User

from time import time
from uuid import uuid4

"""
Use cases encapsulate core domain logic.
"""


class GetUserUseCase(Case):
    def go(self, key: str):
        user_dto = self.repo.get_by_key(key)
        return user_dto


class GetUserByEmailUseCase(Case):
    def go(self, email: str):
        user_dto = self.repo.get_by_email(email)
        return user_dto


class CreateUserUseCase(Case):
    def go(self, data: dict):
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")

        # check required variables are set
        if not (first_name and last_name and email):
            return

        generated_key = uuid4().hex

        # NOTE: `key` and `created_at` could easily be abstracted into our Model Base class
        # They are so common in our codebase I think this would be a reasonable gain
        new_user = User(
            key=f"user_{generated_key}",
            first_name=first_name,
            last_name=last_name,
            email=email,
            created_at=int(time()),
        )

        new_user_dto = new_user.to_dto()

        self.repo.create(new_user_dto)

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

        user_dto = self.repo.update(data)

        return user_dto


class DeleteUserUseCase(Case):
    def go(self, key: str):
        user = self.repo.delete_by_key(key)
