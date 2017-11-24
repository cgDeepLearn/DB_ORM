# -*- coding: utf8 -*-
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .utils import Base


# class User(Base):
#     __tablename__ = 'user'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(32))
#     # 一对多
#     books = relationship('Book')


# class Book(Base):
#     __tablename__ = 'book'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(32))
#     user_id = Column(Integer, ForeignKey('user.id'))

class UserInfo(Base):
    """userinfo 表"""
    __tablename__ = 'userinfo'

    id = Column(Integer, primary_key=True)
    mid = Column(String(20))
    name = Column(String(32))
    fans = Column(Integer)
    videonum = Column(Integer)
    watch = Column(Integer)

    def __repr__(self):
        return "<UserIno(mid=%s,name=%s,fans=%d,videonum=%s,watch=%d)>" % (
            self.mid, self.name, self.fans, self.videonum, self.watch)
