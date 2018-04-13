"""Create DB

Creates the inital Newsboy database
"""

import os

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

DB_DIR = os.path.join(os.environ['APPDATA'], 'Newsboy')
if not os.path.isdir(DB_DIR):
    os.mkdir(DB_DIR)
DB_PATH = os.path.join(DB_DIR, 'newsboy.db')

engine = create_engine(f'sqlite:///{DB_PATH}', echo=False)
Base = declarative_base()


class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    link = Column(String)
    feed_id = Column(String)
    author = Column(String)
    published = Column(String)
    summary = Column(String)


class Subscription(Base):
    __tablename__ = "feed"

    id = Column(Integer, primary_key=True)
    url = Column(String)
    link = Column(String)


Base.metadata.create_all(engine)
