# PLACEHOLDER STORAGE FOR DEVELOPMENT
TABLES = {
    "user": [
        {
            "key": "user_x",
            "fname": "Neil",
            "lname": "Chudleigh",
            "email_address": "nchudleigh@gmail.com",
            "created": 1548617665812,
        }
    ]
}


# TODO: Split this out into two (Perhaps 3) classes?
# 1. Class for modeling the data at the database level (MemRepo)
# 2. A generic "table" class for modeling actions that would be taken on a table (MemRepoObject)
# 3. A class for modeling the unique modifications to Class 2 that are needed for the specific table (MemUserRepo)
class MemRepo:
    def __init__(self):
        if not getattr(self, "babel"):
            raise NotImplementedError("Repos must define a translation map as 'babel'")

    def get_by_key(self, key):
        user = self._get(self.table_name, "key", key)
        return self.to_domain(user)

    def _get(self, table: str, attr: str, val: str):
        for row in TABLES.get(table):
            if row.get(attr) == val:
                return row

    def create(self, data: dict):
        return self._create(self.table_name, data)

    def _create(self, table: str, data: dict):
        row = self.from_domain(data)
        print(row)
        TABLES[table].append(row)
        return self.to_domain(row)

    def to_domain(self, repo_obj: dict):
        domain_obj = {}
        for repo_key, domain_key in self.babel:
            domain_obj[domain_key] = repo_obj.pop(repo_key)
        return self.domain_model(**domain_obj)

    def from_domain(self, domain_obj: dict):
        repo_obj = {}
        for repo_key, domain_key in self.babel:
            repo_obj[repo_key] = domain_obj.pop(domain_key)
        return repo_obj
