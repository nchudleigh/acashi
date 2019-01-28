TABLES = {
    "User": [
        {
            key: "user_x",
            fname: "Neil",
            lname: "Chudleigh",
            email_address: "nchudleigh@gmail.com",
            created: 1548617665812,
        }
    ]
}


class UserMemRepo(MemRepo):
    def get_by_key(self, key):
        self._get("User", "key", key)


class MemRepo:
    def _get(self, model, attr, val):
        for row in TABLES.get(model.table):
            if row.get(attr) == val:
                return row
