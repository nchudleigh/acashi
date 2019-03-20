class ViewRegistrar:
    _allowed_methods = ["get", "post", "delete", "patch", "put"]

    def __init__(self, app):
        self.app = app

    def register_view(self, View):
        view_methods = []

        for method in self._allowed_methods:
            if hasattr(View, method) and callable(getattr(View, method)):
                view_methods.append(method)

        self.register_route(View, methods=view_methods)

    def register_route(self, view, methods):
        self.app.add_url_rule(
            view.path, view_func=view.as_view(view.name), methods=methods
        )
