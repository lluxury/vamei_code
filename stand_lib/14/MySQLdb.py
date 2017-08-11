# http://python.org/topics/database
# https://wiki.python.org/moin/DatabaseInterfaces
# http://blog.csdn.net/column/details/pythontesting.html
MySQLdb（MySQL-Python 或 MySQL Connector/Python (python3)

import MySQLdb
cxn = MySQLdb.connect(user='root')
cxn.query('DROP DATABASE test')
cxn.query('CREATE DATABASE test')
cxn.query("GRANT ALL ON test.* to ''@'localhost'")
cxn.commit()
cxn.close()

# 一些适配器有Connection 对象，这些对象可以使用
# query()方法执行SQL 查询，不过不是所有的适配器都能这样

cxn = MySQLdb.connect(db='test')
cur = cxn.cursor()
cur.execute('CREATE TABLE users(login VARCHAR(8), userid INT)')
cur.execute("INSERT INTO users VALUES('john', 7000)")
cur.execute("INSERT INTO users VALUES('bob', 7200)")
cur.execute("SELECT * FROM users WHERE login LIKE 'j%'")
for data in cur.fetchall():
    print '%s\t%s' % data

cur.execute("UPDATE users SET userid = 7100 WHERE userid=7001")
cur.execute('DELETE FROM users WHERE login = "bob"')
cur.execute('DROP TABLE users')
cur.close()
cxn.commit()
cxn.close()

