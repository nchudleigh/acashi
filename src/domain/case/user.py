from src.domain.case.base import Case, Response
from src.data.user import UserRepo

from time import time
from uuid import uuid4

"""
Use cases encapsulate core domain logic.
"""


class GetUserUseCase(Case):
    def run(self, key):
        user = UserRepo().get_by_key(key)
        return Response(user.to_dict())


class CreateUserUseCase(Case):
    def run(self, data):
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
    def run(self, data):
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
    def run(self, request):
        # permissions checks
        user = UserRepo().get_by_key(key)
        if user.archived:
            # TODO error response
            return
        user = UserRepo().delete_by_key(key)

        return Response(user.to_dict())
