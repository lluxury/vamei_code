#!/usr/bin/env python

from distutils.log import warn as printf
import os
from random import randrange as rand

if isinstance(__builtins__, dict) and 'raw_input' in __builtins__:
    scanf = raw_input
elif hasattr(__builtins__, 'raw_input'):
    scanf = raw_input
else:
    scanf = input

#GOLSIZ = 10
COLSIZ = 10
FIELDS = ('login', 'userid', 'projid')
RDBMSs = {'s': 'sqlite', 'm': 'mysql', 'g':'gadfly'}
DBNAME = 'test'
DBUSER = 'root'
DB_EXC = None
NAMELEN = 16

tformat = lambda s: str(s).title().ljust(COLSIZ)
cformat = lambda s: s.upper().ljust(COLSIZ)

def setup():
    return RDBMSs[scanf('''
Choose a database system:

(M)ySQL
(G)adfly
(S)QLite

Enter choice: ''').strip().lower()[0]]

def connect(db):
    global DB_EXC
    #dbDir = '%s_%s' (db,DBNAME)
    dbDir = '%s_%s' % (db, DBNAME)

    if db == 'sqlite':
        try:
            import sqlite3
        except ImportError:
            try:
                from pysqlite2 import dbapi2 as sqlite3
            except ImportError:
                return None

        DB_EXC = sqlite3
        if not os.path.isdir(dbDir):
            os.mkdir(dbDir)
        cxn = sqlite3.connect(os.path.join(dbDir, DBNAME))

    elif db == 'mysql':
        try:
            import MySQLdb
            import _mysql_exceptions as DB_EXC

            try:
                cxn = MySQLdb.connect(db=DBNAME)
            #except: DB_EXC.OperationalError:
            except DB_EXC.OperationalError:
                try:
                    cxn = MySQLdb.connect(user=DBUSER)
                    cxn.query('CREATE DATABASE %s' % DBNAME)
                    cxn.commit()
                    cxn.close()
                    cxn = MySQLdb.connect(db=DBNAME)
                except DB_EXC.OperationalError:
                    return None
        except ImportError:
            try:
                import mysql.connector
                import mysql.connector.errors as DB_EXC
                try:
                    cxn = mysql.connector.connect(**{
                        'database':DBNAME,
                        'user':DBUSER,
                        })
                except DB_EXC.InterfaceError:
                    return None
            except ImportError:
                return None

    elif db == 'gadfly':
        try:
            from gadfly import gadfly
            DB_EXC = gadfly
        except ImportError:
            return None

        try:
            cxn = gadfly(DBNAME, dbDir)
        except IOError:
            cxn = gadfly()
            if not os.path.isdir(dbDir):
                os.mkdir(dbDir)
            cxn.startup(DBNAME, dbDir)

    else:
        return None
    return cxn

def create(cur):
    try:
        cur.execute('''
            CREATE TABLE users(
            login VARCHAR(%d),
            userid INTEGER,
            projid INTEGER)
            ''' % NAMELEN)
    except (DB_EXC.OperationalError, DB_EXC.ProgrammingError):
        drop(cur)
        create(cur)

drop = lambda cur:cur.execute('DROP TABLE users')

NAMES = (
    ('aaron', 8312), ('angela', 7603), ('dave', 7306),
    ('davina',7902), ('elliot', 7911), ('ernie', 7410),
    ('jess', 7912), ('jim', 7512), ('larry', 7311),
    ('leslie', 7808), ('melissa', 8602), ('pat', 7711),
    ('serena', 7003), ('stan', 7607), ('faye', 6812),
    ('amy', 7209), ('mona', 7404), ('jennifer', 7608),
)


def randName():
    pick = set(NAMES)
    while pick:
        yield pick.pop()

def insert(cur, db):
    if db ==  'sqlite':
        cur.executemany("INSERT INTO users VALUES(?, ?, ?)",
            [(who, uid, rand(1,5)) for who, uid in randName()])
    elif db == 'gadfly':
        for who, uid in randName():
            cur.execute("INSERT INTO users VALUES(?, ?, ?)",
            (who, uid, rand(1,5)))
    elif db == 'mysql':
        cur.executemany("INSERT INTO users VALUES(%s, %S, %S)",
            [(who, uid, rand(1,5)) for who, uid in randName()])

getRC = lambda cur:cur.rowcount if hasattr(cur, 'rowcount') else -1

def update(cur):
    fr = rand(1,5)
    to = rand(1,5)
    cur.execute(
        "UPDATE users SET projid =%d WHERE projid=%d" % (to, fr))
    return fr, to, getRC(cur)

def delete(cur):
    rm = rand(1,5)
    cur.execute('DELETE FROM users WHERE projid=%d' % rm)
    return rm, getRC(cur)

def dbDump(cur):
    #cur.execute('SELETC * FROM users')
    cur.execute('SELECT * FROM users')
    printf('\n%s' % ''.join(map(cformat, FIELDS)))
    for data in cur.fetchall():
        printf(''.join(map(tformat, data)))

def main():
    db = setup()
    printf('*** connect to %r database' % db)
    cxn = connect(db)
    if not cxn:
        printf('ERROR: %r not supported or unreachable, exit' % db)
        return
    cur = cxn.cursor()

    printf('\n*** Create users table')
    #creat(cur)
    create(cur)

    printf('\n*** Insert names into table')
    insert(cur, db)
    dbDump(cur)

    printf('\n*** Move user to a random group')
    fr, to, num = update(cur)
    printf('\t(%d users moved) from (%d) to (%d)' % (num, fr, to))
    dbDump(cur)

    printf('\n*** Randonly delete group')
    rm,num = delete(cur)
    printf('\t(group #%d; %d users remove)' % (rm, num))
    dbDump(cur)

    printf('\n*** Drop users table')
    drop(cur)
    printf('\n*** Close cxns')
    cur.close()
    cxn.commit()
    cxn.close()

if __name__ == '__main__':
    main()



# 需要重新编译 yum install sqlite-devel -y 然后编译py3
# tformat() cformat() setup()
# 如果存在raw_input使用,不然使用input py3
# __builtins__应用模块,成为字典
# 格式化函数,标题样式及全大写,左对齐,宽度10 统一名字
# distutils.log.warn() 做输出函数?
# DB_EXC数据库异常, 不同库不同异常 (_mysql_exceptions)
# 找sqlite 或第3方包,可以基于文件或内存:memory:
# MySQLdb或 mysql.connector

# 建表,如果存在删表再执行, 存在死循环风险
# 常量NAMES, 生成器randName()?
# SQLite MySQL适配器都是兼容DB-API 的，所以它们的游标对象都存在executemany()函数
# SQLite 使用qmark 参数风格，MySQL 使用format参数风格
# 户名-id分配到一个项目组中,给不同的projid

# getRC条件表达式（也可以解读为是Python 的三元操作符），用于返回最后一次操
# 作后影响的行数，不过如果游标对象不支持该属性（即不兼容DB-API），则返回−1

# 更新,删除. 
# 导出,打印. 迭代每个用户,3列通过map()传给tformat(),格式化并转为字符串 

# 执行函数,定义执行方法,最后把游标和连接cxn