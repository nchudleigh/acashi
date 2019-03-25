from src.handler import Handler, Response
from src.domain.case.user import GetUserByEmailUseCase
from src.domain.case.password import GetPasswordByUserKeyUseCase
from src.data.user import UserRepo
from src.data.password import PasswordRepo
from src.domain.case.token import EncodeTokenUseCase, DecodeTokenUseCase
from src.library.token import TokenRepo


class LoginHandler(Handler):
    def go(self):
        # XXX: placeholder
        email = "nchudleigh@gmail.com"
        password_attempt = "aaaaaaaaaaah"

        # retrieve user key based on given email
        get_user_by_email = GetUserByEmailUseCase(UserRepo)
        user_dto = get_user_by_email.go(email)

        # retrieve password based on user key
        get_password_by_user_key = GetPasswordByUserKeyUseCase(PasswordRepo)
        password_dto = get_password_by_user_key.go(user_dto.key)

        # check given password against stored
        check_password = CheckPasswordUseCase(PasswordRepo)
        check_password.go(password_attempt, password_dto)

        # create token
        create_token = EncodeTokenUseCase(TokenRepo)
        token = create_token.go(user_dto)

        return Response(message="Logged in", data=token)


class DecodeTokenHandler(Handler):
    def go(self, encoded_token):
        decode_token = DecodeTokenUseCase(TokenRepo)
        token = decode_token.go(encoded_token)
        return Response(message="Token decoded", data=token)
