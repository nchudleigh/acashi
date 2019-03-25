from src.data import MemRepo
from src.domain.model.user import UserDTO


class UserRepo(MemRepo):
    DTO = UserDTO
    table_name = "user"

    def get_by_email(self, email):
        return self.get_by_attr("email", email)
