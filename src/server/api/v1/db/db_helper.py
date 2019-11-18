from abc import ABC, abstractmethod

from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session

from .db_models import UserModel, DeclarativeBase


class DBHelperBase(ABC):

    @abstractmethod
    def create(self, *args):
        pass

    @abstractmethod
    def update(self, *args):
        pass

    @abstractmethod
    def delete(self, *args):
        pass


class UserDBHelper(DBHelperBase):
    def __init__(self, connection):
        self._db_connection = connection

    def create(self, name, passwd, token=None):
        user_obj = UserModel(nickname=name, passwd=passwd, token=token)
        self._db_connection.add(user_obj)
        self._db_connection.commit()

    @staticmethod
    def update(uid, data):
        db_connection.query(UserModel).filter(UserModel.id == uid).update(data)

    def delete(self):
        pass

    @staticmethod
    def user_exists(data):
        return db_connection.query(UserModel).filter_by(nickname=data.get('nickname')).first()


class SessionDBHelper(DBHelperBase):
    def __init__(self, connection):
        self._db_connection = connection

    def create(self, user_session):
        pass

    def update(self):
        pass

    def delete(self):
        pass


engine = create_engine("sqlite:///warshipbattle.sqlite")
db_connection = Session(bind=engine)
DeclarativeBase.metadata.create_all(engine)
