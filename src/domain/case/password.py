from src.domain.case import Case
from src.domain.model.password import Password
from src.library.crypt_keeper import CryptKeeper


class GetPasswordByUserKeyUseCase(Case):
    def go(self, user_key):
        password_repo = self.PasswordRepo()
        password_dto = password_repo.get_by_user_key(user_key)
        return password_dto


class SetPasswordUseCase(Case):
    def go(self, password, user_key):
        crypt_keeper = self.CryptKeeper()
        password_repo = self.PasswordRepo()

        hashed_password, salt = crypt_keeper.hash_password(password)

        new_password = Password(hashed=hashed_password, salt=salt, user_key=user_key)

        new_password_dto = new_password.to_dto()

        password_repo.create(new_password_dto)

        return new_password_dto


class CheckPasswordUseCase(Case):
    def go(self, password_attempt, password):
        crypt_keeper = self.CryptKeeper()

        is_valid = crypt_keeper.check_password(
            password_attempt, password.hashed, password.salt
        )

        message = "Password is valid" if is_valid else "Password is invalid"

        return is_valid
