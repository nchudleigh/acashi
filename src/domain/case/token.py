from src.domain.case import Case


class EncodeTokenUseCase(Case):
    def go(self, user):
        payload = {"id": user.id, "key": user.key}
        token = self.repo.encode_payload(payload)
        return token


class DecodeTokenUseCase(Case):
    def go(self, token):
        token = self.repo.decode_token(token)
        return token
