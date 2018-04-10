import os
from sqlalchemy import create_engine

DB_DIR = os.path.join(os.environ['APPDATA'], 'Newsboy')
if not os.path.isdir(DB_DIR):
    os.mkdir(DB_DIR)
DB_PATH = os.path.join(DB_DIR, 'newsboy.db')

engine = create_engine(f'sqlite:///{DB_PATH}')

with engine.connect() as con:
    articles = con.execute("SELECT id, title, link FROM article")
    data = articles.fetchall()
    print(data)
