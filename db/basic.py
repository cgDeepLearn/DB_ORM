import os
from config import get_db_args, get_db_type

RDBMSs = {'s':'sqlite', 'm':'mysql', 'p':'postgresql'}
DB_EXCEPTION = None


def setup1():
    return RDBMSs[input('''
choose a database system:

(M)ySQL
(P)ostgreSQL)
(S)QLite

Enter choice: ''').strip().lower()[0]]

class myDataBase(object):
    """数据库类，可根据db_index选择不同的数据库"""
    def __init__(self, db_index=0):
        """
        dbindex: 0-mysql,1-postgresql,2-sqlite
        默认为mysql数据库
        """
        self.dbtype = get_db_type(db_index)
        self.dbargs = get_db_args(self.dbtype)

    def connect(self):
        global DB_EXCEPTION
        DBNAME = self.dbargs['dbname']
        dbDir = '%s_%s' % (self.dbtype, DBNAME)

        if self.dbtype == 'sqlite':
            import sqlite3

            DB_EXCEPTION = sqlite3
            if not os.path.isdir(dbDir):
                os.mkdir(dbDir)
            conn = sqlite3.connect(os.path.join(dbDir, DBNAME))
        
        elif self.dbtype == 'mysql':
            import pymysql
            DB_EXCEPTION = pymysql
            
            args = ('host','user','password','database','port')
            values = (self.dbargs['host'], self.dbargs['user'],self.dbargs['password'],
                        self.dbargs['dbname'], int(self.dbargs['port']))
            kwargs = dict(zip(args, values))

            try:
                conn = pymysql.connect(**kwargs)
            except DB_EXCEPTION.InterfaceError:
                return None
        
        elif self.dbtype == 'postgresql':
            import psycopg2
            DB_EXCEPTION = psycopg2

            args = ('host','user','password','database','port')
            values = (self.dbargs['host'], self.dbargs['user'],self.dbargs['password'],
                        self.dbargs['dbname'],self.dbargs['port'])
            kwargs = dict(zip(args, values))

            try:
                conn = psycopg2.connect(**kwargs)
            except DB_EXCEPTION.InterfaceError:
                return None
        else:
            return None

        return conn

    def create():

            

