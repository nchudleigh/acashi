from src.rest.user import UserView


def register_routes(app):
    UserView().register(app, "users", "/users/<key>")
