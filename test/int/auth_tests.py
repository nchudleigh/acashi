from test import TestCase
from src.handler.auth import DecodeTokenHandler
from src.library.token import TokenRepo, DecodeError


class DecodeToken(TestCase):
    @classmethod
    def setUpClass(self):
        self.valid_token_payload = {"user_id": 1, "user_key": "user_xxx"}
        self.valid_encoded_token = TokenRepo().encode_payload(self.valid_token_payload)
        self.invalid_encoded_token = b"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VyX2tleSI6InVzZXJfeHh4In0.Uv80VcHfm6dZx-GnUbrIVQFEdBPxEKnddddd3pEKd"
        print(self.valid_encoded_token)

    def test_successful(self):
        decode_token = DecodeTokenHandler()
        response = decode_token.run(self.valid_encoded_token)
        self.assertEqual(response.data, self.valid_token_payload)

    def test_invalid_token(self):
        decode_token = DecodeTokenHandler()
        try:
            decode_token.run(self.invalid_encoded_token)
        except DecodeError as e:
            self.assertTrue(isinstance(e, DecodeError))
