class Request:
    def __init__(self, data):
        self.data = data


class Response:
    def __init__(self, data):
        self.data = data


class Case:
    def __init__(self, Repo):
        if Repo:
            self.repo = Repo()

    def run(self, *args, **kwargs):
        return self.go(*args, **kwargs)

    def go(self):
        raise NotImplementedError()
