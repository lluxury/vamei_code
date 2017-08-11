# 适配器内置,数据库需要安装
import sqlite3
# cnx = sqlite3.connect('sqlite_text/test')
cnx = sqlite3.connect('test')   #/var/microblog/test
cur = cxn.cursor()
cur.execute('CREATE TABLE users(login VARCHAR(8),userid INTEGER)')
cur.execute('INSERT INTO users VALUES("john", 100)')
cur.execute('SELECT * FROM users')
for eachUser in cur.fetchall():
    print eachUser
cur.execute('DROP TABLE users')
cur.close()
cnx.commit()
cnx.close()

