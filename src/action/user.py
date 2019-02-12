from src.domain.case.user import GetUserUseCase
from src.data.user import UserRepo

"""
Actions mesh the data layer and the domain layer.
More specifcally they initialize the Repo and register it to the UseCase.
They then handle executing the UseCase, and giving back a response.

They may just return the Response that the UseCase gives in a simple CRUD case.
Or format their own Response if they are composing multiple usecases or need to be more custom.

They could be seen as a proxy, to keep the presentation layer and the domain layer separate from each other.
"""


def GetUserAction(key):
    r = UserRepo()
    uc = GetUserUseCase(r)
    return uc.go(key)


def CreateUserAction(data):
    r = UserRepo()
    uc = CreateUserUseCase(r)
    return uc.go(data)
