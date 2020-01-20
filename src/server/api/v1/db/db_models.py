from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.types import PickleType

DeclarativeBase = declarative_base()


class UserModel(DeclarativeBase):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(20), nullable=False, unique=True)
    passwd = Column(String(30), nullable=False)
    token = Column(String())


class SessionModel(DeclarativeBase):
    __tablename__ = "session"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey("user.id"))
    session = Column(PickleType)
    user = relationship("UserModel", backref="session")
