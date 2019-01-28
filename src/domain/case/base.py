class Case:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, data):
        if not data:
            return res.ResponseFailure.build_from_invalid_data(data)
        try:
            return self.run(data)
        except Exception as exc:
            return res.ResponseFailure.build_system_error(
                "{}: {}".format(exc.__class__.__name__, "{}".format(exc))
            )

    def run(self):
        raise NotImplementedError()
