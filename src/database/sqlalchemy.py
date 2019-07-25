import sqlalchemy
from sqlalchemy import orm


def create_engine(url, echo=True):
    return sqlalchemy.create_engine(url, echo=echo)


def create_session_class(engine):
    return orm.sessionmaker(bind=engine)

