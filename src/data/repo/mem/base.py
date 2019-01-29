# MOCK STORAGE FOR DEVELOPMENT
TABLES = {
    "User": [
        {
            "key": "user_x",
            "fname": "Neil",
            "lname": "Chudleigh",
            "email_address": "nchudleigh@gmail.com",
            "created": 1548617665812,
        }
    ]
}
# MOCK STORAGE FOR DEVELOPMENT


class MemRepo:
    def __init__(self):
        if not getattr(self, "babel"):
            raise NotImplementedError("Repos define a translation map as 'babel'")

    def _get(self, table: str, attr: str, val: str):
        for row in TABLES.get(table):
            if row.get(attr) == val:
                return row

    def to_domain(self, repo_obj: dict):
        for k, v in self.babel:
            repo_obj[v] = repo_obj.pop(k)
        return self.domain_model(**repo_obj)

    def from_domain(self, domain_obj: dict):
        for k, v in self.babel:
            domain_obj[v] = domain_obj.pop(k)
        return domain_obj
