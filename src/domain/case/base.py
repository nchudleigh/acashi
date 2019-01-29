class Response:
    def __init__(self, data):
        self.data = data


class Case:
    def execute(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def run(self):
        raise NotImplementedError()
