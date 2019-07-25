from sqlalchemy import Column, String, Boolean, BigInteger, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import as_declarative, declared_attr

print("init: dao.base")


@as_declarative()
class BaseDAO(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.replace("DAO", "").lower()

    @classmethod
    def getKey(self, key):
        return self.query.filter_by(key=key).first()

    def __repr__(self):
        return f"<{self.__tablename__} {self.key}>"

