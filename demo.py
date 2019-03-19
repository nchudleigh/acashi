# domain object, innermost
# will move a bunch of this functionality in to the base but have left in for clarity
# TODO: DTO implementation
class User(Model):
    def __init__(self, key, first_name, last_name, email, created_at):
        self.key = key
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = created_at

    def to_dict(self):
        return {
            "key": self.key,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "created_at": self.created_at,
        }

    def __eq__(self, other):
        return self.to_dict() == other


class CreateUserUseCase(Case):
    # a usecase should have a single purpose
    # it will be initialized with a repository in most cases
    # this repo is initialized in the init function and pinned to self.repo

    def validate(self, data):
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")

        # check required variables are set
        if not (first_name and last_name and email):
            raise ValueError("Required values not given")

    def run(self, data):
        self.validate()

        generated_key = uuid4().hex

        new_user = User(
            key=f"user_{generated_key}",
            first_name=first_name,
            last_name=last_name,
            email=email,
            created_at=int(time()),
        )

        user = self.repo.create(new_user)

        return Response(data=user)


# this is the implementation of the in memory repository
# you can see on create it is converting from the domain object to a plain `dict`
# it is then storing that to the table_name given in the super classes definition
class MemRepo:
    def __init__(self):
        if not getattr(self, "babel"):
            raise NotImplementedError(
                "MemRepos must define a translation map as 'babel'"
            )
        if not getattr(self, "domain_model"):
            raise NotImplementedError("MemRepos must register a 'domain_model'")
        if not getattr(self, "table_name"):
            raise NotImplementedError(
                "MemRepos must register a 'table_name', this is the key that the data will be stored at"
            )

    def create(self, data: dict):
        return self._create(self.table_name, data)

    def _create(self, table: str, data: dict):
        row = self.from_domain(data)
        TABLES[table].append(row)
        return

    def to_domain(self, repo_obj: dict):
        domain_obj = {}
        for repo_key, domain_key in self.babel:
            domain_obj[domain_key] = repo_obj.pop(repo_key)
        return self.domain_model(**domain_obj)


class UserRepo(MemRepo):
    # example of a translation implementation
    # on create this would convert the domain model to the
    # format needed for this particular repo
    # on retrieve, the opposite
    babel = (
        ("fname", "first_name"),
        ("lname", "last_name"),
        ("email_address", "email"),
        ("created", "created_at"),
    )
    # registering the domain model
    domain_model = User
    # a repo specific piece of data
    # based on the type of repo this oculd be completely different
    # eg. a redis repo may have a key pattern instead
    table_name = "user"


class CreateUserHandler(Handler):
    # handlers bring together repos and usecases
    # they will initialize the repo and the usecase
    # register them together, run the usecase and surface the response
    # it would be at this layer we would implement access control
    def go(self):
        r = UserRepo()
        uc = CreateUserUseCase(r)
        return uc.go(data)


class UserView(BaseView):
    # views are repsonsible for transating to and from http/json
    # they will initialize a handler and call it, returning the response
    # the internals of BaseView handle the translation of errors
    def post(self, request):
        handler = CreateUserHandler()
        response = handler.go(request.data)
        return response
