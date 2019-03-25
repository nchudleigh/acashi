from src.data import MemRepo
from src.domain.model.password import PasswordDTO


class PasswordRepo(MemRepo):
    DTO = PasswordDTO
    table_name = "password"
