from src.data.dao.base import (
    BaseDAO,
    Column,
    String,
    Boolean,
    BigInteger,
    Integer,
    ForeignKey,
    relationship,
)

print("init: src.data.dao.password")


class PasswordDAO(BaseDAO):
    key = Column(String(25), primary_key=True, index=True)
    user_key = Column(String(40))

    created_at = Column(BigInteger())

    salt = Column(String(255))
    hashed_password = Column(String(255))

