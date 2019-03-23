class Handler:
    def __init__(self):
        go_func = getattr(self, "go")
        if not go_func and callable(go_func):
            raise NotImplementedError("Handler's must define a go function")
