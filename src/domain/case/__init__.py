class Request:
    def __init__(self, data):
        self.data = data


class Response:
    def __init__(self, data, success=True):
        self.data = data
        self.success = success

    def __dict__(self):
        if hasattr(data, "_asdict"):
            return data._asdict()


class Case:
    def __init__(self, Repo):
        if Repo:
            self.repo = Repo()

    def run(self, *args, **kwargs):
        return self.go(*args, **kwargs)

    def go(self):
        raise NotImplementedError()
