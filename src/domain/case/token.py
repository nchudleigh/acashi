from src.domain.case import Case


class EncodeTokenUseCase(Case):
    def go(self, user):
        payload = {"id": user.id, "key": user.key}
        token_repo = self.TokenRepo()
        token = self.encode_payload(payload)
        return token


class DecodeTokenUseCase(Case):
    def go(self, token):
        token_repo = self.TokenRepo()
        token = token_repo.decode_token(token)
        return token
