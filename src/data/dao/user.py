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

print("init: src.data.dao.user")


class UserDAO(BaseDAO):
    key = Column(String(25), primary_key=True, index=True)
    created_at = Column(BigInteger())
    name = Column(String(255), index=True)
