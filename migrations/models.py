from sqlalchemy import Column, Integer, String, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# metadata = MetaData()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    created_at = Column(DateTime)
    deleted_at = Column(DateTime)


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True)
    following_user_id = Column(Integer)
    title = Column(String)
    target_day = Column(String)  # SQLAlchemyの型に合わせてStringを使用
    notice_time = Column(DateTime)
    created_at = Column(DateTime)
    deleted_at = Column(DateTime)
