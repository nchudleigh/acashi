from pprint import pprint

from src.rest.registrar import ViewRegistrar
from src.rest.user import CreateUserView, UserView


def register_views(app):
    view_registrar = ViewRegistrar(app)
    view_registrar.register_view(UserView)
    view_registrar.register_view(CreateUserView)
    # print registered routes
    # pprint([rul for rul in app.url_map.iter_rules()])
