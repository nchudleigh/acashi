from src.domain.case.base import Case, Response
from src.domain.model.user import User

from time import time
from uuid import uuid4

"""
Use cases encapsulate core domain logic.
"""


class GetUserUseCase(Case):
    def go(self, key):
        user = self.repo.get_by_key(key)
        return Response(user.to_dict())


class CreateUserUseCase(Case):
    def go(self, data):
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")

        # check required variables are set
        if not (first_name and last_name and email):
            return

        generated_key = uuid4().hex

        payload = {
            "key": f"user_{generated_key}",
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "created_at": int(time()),
        }

        user = self.repo.create(payload)

        return Response()


class UpdateUserUseCase(Case):
    def go(self, data):
        # check required variables are set
        if (
            data.get("first_name") is None
            and data.get("last_name") is None
            and data.get("email") is None
        ):
            # TODO: error response
            return

        user = self.repo.update(data)

        return Response(user.to_dict())


class DeleteUserUseCase(Case):
    def go(self, request):
        # permissions checks
        user = self.repo().get_by_key(key)
        if user.archived:
            # TODO error response
            return
        user = UserRepo().delete_by_key(key)

        return Response(user.to_dict())
