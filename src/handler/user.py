from src.handler import Handler
from src.domain.case.user import GetUserUseCase
from src.data.user import UserRepo

"""
Actions mesh the data layer and the domain layer.
More specifcally they initialize the Repo and provide it to the UseCase.
They then handle executing the UseCase, and giving back a response.

They may just return the Response that the UseCase gives in a simple CRUD case.
Or format their own Response if they are composing multiple usecases or need to be more custom.

They could be seen as a proxy, to keep the presentation layer and the domain layer separate from each other.
"""


class GetUserHandler(Handler):
    def go(self):
        # probably abstracted within Handler or similar class
        auth_repo = AuthRepo()
        user_is_authenticated_uc = UserIsAuthenticatedUseCase(auth_repo)
        user_is_authenticated_uc.go(token)
        # end of auth

        user_repo = UserRepo()
        get_user_uc = GetUserUseCase(user_repo)
        return get_user_uc.go(key)


class CreateUserHandler(Handler):
    def go(self):
        r = UserRepo()
        uc = CreateUserUseCase(r)
        return uc.go(data)
