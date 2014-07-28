# coding: UTF-8

from sqlalchemy import (
    Column,
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


# イベントテーブル
class Event(Base):
    STATUS_ACTIVE = 1
    STATUS_DEACTIVE = 0

    __tablename__ = 't_events'
    _id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    hash_id = Column(Text, nullable=False)
    detail_comment = Column(Text)
    start_at = Column(Text, nullable=False)
    end_at = Column(Text, nullable=False)
    status = Column(Integer, default=1)

    def __init__(self, name, hash_id, detail_comment, start_at, end_at):
        self.name = name
        self.hash_id = hash_id
        self.detail_comment = detail_comment
        self.start_at = start_at
        self.end_at = end_at


# ユーザテーブル,イベントに紐付く
class User(Base):
    __tablename__ = "m_users"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    event_id = Column(Integer, nullable=False)

    def __init__(self, name, event_id):
        self.name = name
        self.event_id = event_id


# 日にちテーブル,ユーザの一日の状態を示す
class Date(Base):
    STATUS_ACTIVE = 1
    STATUS_DEACTIVE = 0

    __tablename__ = "t_dates"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Text, nullable=False)
    user_id = Column(Integer, nullable=False)
    event_id = Column(Integer, nullable=False)
    status = Column(Integer)

    def __init__(self, date, user_id, event_id, status):
        self.date = date
        self.user_id = user_id
        self.event_id = event_id
        self.status = status
