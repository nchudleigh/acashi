from src.data.dao.password import PasswordDAO
from src.data.dao.user import UserDAO
from src.data.dao.base import BaseDAO

from db.sqlalchemy import create_engine, create_session_class
from src.library.profile import profiled


def init_db():
    """
        This is specific to the entry point, in this case we want just an in memory sqlite engine
        Creating it from scratch each time we run
    """

    engine = create_engine("sqlite:///:memory:", echo=False)

    BaseDAO.metadata.create_all(engine)

    Session = create_session_class(engine)

    session = Session()

    return session


if __name__ == "__main__":
    with profiled():
        session = init_db()

        user = UserDAO(key="user_xxx", created_at=1232133, name="Neil")

        password = PasswordDAO(
            key="pass_xxx", user_key=user.key, hashed_password="xxx", salt="himilayan"
        )
        password2 = PasswordDAO(
            key="pass_yyy", user_key=user.key, hashed_password="yyy", salt="kosher"
        )
        password3 = PasswordDAO(
            key="pass_zzz", user_key=user.key, hashed_password="zzz", salt="table"
        )

        session.add_all([user, password, password2, password3])
        passwords = (
            session.query(PasswordDAO).filter(PasswordDAO.user_key == user.key).all()
        )
        print(passwords)
        print(session.new)
        print(session.dirty)
