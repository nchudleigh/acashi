class Request:
    def __init__(self, data):
        self.data = data


class Response:
    def __init__(self, data):
        self.data = data


class Case:
    def __init__(self, repo=None):
        if repo:
            self.repo = repo

    def go(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def run(self):
        raise NotImplementedError()
