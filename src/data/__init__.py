from src.data.exceptions import NotFoundError

# PLACEHOLDER STORAGE FOR DEVELOPMENT
TABLES = {
    "user": [
        {
            "key": "user_x",
            "first_name": "Neil",
            "last_name": "Chudleigh",
            "email": "nchudleigh@gmail.com",
            "created_at": 1_548_617_665_812,
        }
    ]
}


# TODO: Split this out into two (Perhaps 3) classes?
# 1. Class for modeling the data at the database level (MemRepo)
# 2. A generic "table" class for modeling actions that would be taken on a table (MemRepoObject)
# 3. A class for modeling the unique modifications to Class 2 that are needed for the specific table (MemUserRepo)
class MemRepo:
    def __init__(self):
        if not getattr(self, "DTO"):
            raise NotImplementedError("Repos must define a DTO pinned to self")

    def get_by_key(self, key):
        row = self._get(self.table_name, "key", key)
        if row is None:
            raise NotFoundError(
                f"Could not find a record in {self.table_name} for key {key}"
            )
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
        return self.DTO(**repo_obj)

    def from_dto(self, dto):
        return dto._asdict()
