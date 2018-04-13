from create_db import engine, Article
from sqlalchemy.sql import select


conn = engine.connect()
s = select([Article])
print(str(s))
result = conn.execute(s)
for row in result.fetchall():
    print(row)
