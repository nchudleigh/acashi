from src.domain.case import Case, Response
from src.domain.model.user import Password
from src.libraries.crypt_keeper import CryptKeeper


class SetPasswordUseCase(Case):
    def go(self, password, user_key):
        crypt_keeper = CryptKeeper()

        hashed_password, salt = crypt_keeper.hash_password(password)

        new_password = Password(
            hashed=hashed_password,
            salt=salt
            user_key=user_key
        )

        new_password_dto = new_password.to_dto()

        self.repo.create(new_password_dto)

        return Response("New password set")

class CheckPasswordUseCase(Case):
    def go(self, password_attempt, password_key):

        crypt_keeper = CryptKeeper()

        password = self.repo.get(password_key)

        successful = crypt_keeper.check_password(password_attempt, password.hashed, password.salt)

        message = "Password is valid" if successful else "Password is invalid"

        return Response(message, success=successful)
