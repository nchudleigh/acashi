class Payload:
    def __init__(self, data):
        self.data = data


# TODO find a name for this that doesnt conflict with view layer
class Response:
    def __init__(self, message, data, success=True):
        self.message = message
        self.data = data
        self.success = success

    def __dict__(self):
        if hasattr(data, "_asdict"):
            return data._asdict()


class Handler:
    def __init__(self):
        go_func = getattr(self, "go")
        if not go_func and callable(go_func):
            raise NotImplementedError("Handler must define a go function")

    def run(self, *args, **kwargs):
        return self.go(*args, **kwargs)
