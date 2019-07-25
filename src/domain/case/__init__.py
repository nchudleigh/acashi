class Case:
    def __init__(self, *kw):
        for repo_name, RepoClass in kw.items():
            if getattr(RepoClass, is_repo, False):
                setattr(self, repo_name, RepoClass)

    def run(self, *args, **kwargs):
        return self.go(*args, **kwargs)

    def go(self):
        raise NotImplementedError("Cases must implement a go function")
