from src.handler import Handler, Response
from src.domain.case.user import GetUserUseCase
from src.data.user import UserRepo

"""
Handlers mesh the data layer and the domain layer.
More specifcally they initialize the Repo and provide it to the UseCase.
They then handle executing the UseCase, and giving back a response.

They may just return the Response that the UseCase gives in a simple CRUD case.
Or format their own Response if they are composing multiple usecases or need to be more custom.

They could be seen as a proxy, to keep the presentation layer and the domain layer separate from each other.
"""


class GetUserHandler(Handler):
    def go(self, key):
        get_user_usecase = GetUserUseCase(UserRepo=UserRepo)
        user = get_user_usecase.run(key)
        return Response("Got User", user)


class CreateUserHandler(Handler):
    def go(self, payload):
        create_user = CreateUserUseCase(UserRepo=UserRepo)
        create_user.run(payload.data)
        return Response("Created User", user)
