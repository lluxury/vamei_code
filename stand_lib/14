
# Python标准库中的sqlite3提供该数据库的接口
# 一个简单的关系型数据库，为一个书店存储书的分类和价格
# 数据库中包含两个表：category用于记录分类，book用于记录某个书的信息。一本书归属于某一个分类，book有一个外键(foreign key)，指向catogory表的主键id

外键 id int - category int

# By Vamei
import sqlite3

# test.db is a file in the working directory.
conn = sqlite3.connect("test.db")

c = conn.cursor()

# create tables
c.execute('''CREATE TABLE category
      (id int primary key, sort int, name text)''')
c.execute('''CREATE TABLE book
      (id int primary key, 
       sort int, 
       name text, 
       price real, 
       category int,
       FOREIGN KEY (category) REFERENCES category(id))''')

# save the changes
conn.commit()

# close the connection with the database
conn.close()

# SQLite的数据库是一个磁盘上的文件test.db，因此整个数据库可以方便的移动或复制


插入数据
# By Vamei

import sqlite3

conn = sqlite3.connect("test.db")
c    = conn.cursor()

books = [(1, 1, 'Cook Recipe', 3.12, 1),
            (2, 3, 'Python Intro', 17.5, 2),
            (3, 2, 'OS Intro', 13.6, 2),
           ]

# execute "INSERT" 
c.execute("INSERT INTO category VALUES (1, 1, 'kitchen')")

# using the placeholder
#c.execute("INSERT INTO category VALUES (?, ?, ?)", [(2, 2, 'computer')])
c.execute("INSERT INTO category VALUES (?, ?, ?)", (2, 2, 'computer'))

# execute multiple commands
c.executemany('INSERT INTO book VALUES (?, ?, ?, ?, ?)', books)

conn.commit()
conn.close()

# SQL语句中的参数，使用"?"作为替代符号，并在后面的参数中给出具体值 这里不能用Python的格式化字符串，如"%s"，因为这一用法容易受到SQL注入攻击
#注意有一个插入的技巧,

查询
# 在执行查询语句后，Python将返回一个循环器，包含有查询获得的多个记录。循环读取，也可以使用sqlite3提供的fetchone()和fetchall()方法读取记录
# By Vamei

import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

# retrieve one record
c.execute('SELECT name FROM category ORDER BY sort')
print(c.fetchone())
print(c.fetchone())

# retrieve all records as a list
c.execute('SELECT * FROM book WHERE book.category=1')
print(c.fetchall())

# iterate through the records
for row in c.execute('SELECT name, price FROM book ORDER BY sort'):
    print(row)


更新与删除
# By Vamei

conn = sqlite3.connect("test.db")
c = conn.cursor()

c.execute('UPDATE book SET price=? WHERE id=?',(1000, 1))
c.execute('DELETE FROM book WHERE id=2')

conn.commit()
conn.close()

# 直接删除整张表：如果删除test.db，那么物理数据库会被删除
c.execute('DROP TABLE book')

