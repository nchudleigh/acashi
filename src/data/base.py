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
        row = self._get(self.table_name, "key", key)
        return self.to_dto(row)

    def _get(self, table: str, attr: str, val: str):
        for row in TABLES.get(table):
            if row.get(attr) == val:
                return row

    def create(self, dto):
        self._create(self.table_name, dto)

    def _create(self, table: str, dto):
        row = dto._asdict()
        TABLES[table].append(row)

    def to_dto(self, repo_obj: dict):
        for repo_key, dto_attr in self.babel:
            repo_obj[dto_attr] = repo_obj[repo_key]
            del repo_obj[repo_key]

        return self.DTO(**repo_obj)

    def from_dto(self, dto):
        repo_obj = {}
        for dto_attr, dto_value in dto:
            repo_obj[dto_attr] = dto_value

        for repo_key, dto_attr in self.babel:
            repo_obj[repo_key] = repo_obj[dto_attr]
            del repo_obj[dto_attr]

        return repo_obj
