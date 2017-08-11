# psycopg、PyPgSQL 和PyGreSQL
import psycopg
cxn = psycopg.connect(user='pgsql')
cur = cxn.cursor()
cur.execute('SELECT * FROM pg_database')
rows = cur.fetchall()
for i in rows:
    print i
cur.close()
cxn.commit()
cxn.close()

# 不同适配器输出结果不同
