from src.rest.user import UserView


def register_routes(app):
    # registers all routes that are at this /users/<key> route
    UserView().register(app, "users", "/users/<key>")
