# coding: UTF-8

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


#イベントテーブル
class Event(Base):
    __tablename__ = 't_events'
    _id = Column(Integer,primary_key=True)
    name = Column(Text , nullable=False)
    hash_id = Column(Text, nullable=False)
    created_at = Column(Text, nullable=False)
    completed_at = Column(Text)
    status = Column(Integer, default=1)


#ユーザテーブル,イベントに紐付く
class User(Base):
    __tablename__ = "m_users"
    _id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(Text , nullable=False)
    event_id = Column(Integer , nullable=False)


#日にちテーブル,ユーザの一日の状態を示す
class Date(Base):
    __tablename__ = "t_dates"
    _id = Column(Integer , primary_key=True, autoincrement=True)
    date = Column(Text , nullable=False)
    user_id = Column(Integer , nullable=False)
    event_id = Column(Integer , nullable=False)
    status = Column(Integer , default=1)


# Index('my_index', MyModel.name, unique=True, mysql_length=255)
