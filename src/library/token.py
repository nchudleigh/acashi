import jwt


class DecodeError(Exception):
    pass


class EncodeError(Exception):
    pass


class TokenRepo:
    def __init__(self):
        self.secret = "placeholder"
        self.algorithm = "HS256"

    def encode_payload(self, payload: dict) -> str:
        """Encodes payload returns token"""
        try:
            return jwt.encode(payload, self.secret, self.algorithm)
        except Exception as e:
            raise EncodeError(str(e))

    def decode_token(self, token: str) -> dict:
        """Decodes token returns payload"""
        try:
            return jwt.decode(token, self.secret, algorithms=[self.algorithm])
        except Exception as e:
            raise DecodeError(str(e))
