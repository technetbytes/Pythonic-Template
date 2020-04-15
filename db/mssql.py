from sqlalchemy import create_engine
from db import connection
from  utilities import constant
from db import dbbase

class MsSqlDb(dbbase.DBCore):
    '''This core class provide supporting function (CRUD Operations) for MS SQL Server.'''
    
    def __init__(self, connection_str):
        if connection_str is None:
            dbbase.DBCore.__init__(self,connection.ConnectionString(constant.DB_TYPE_MSSQL_SERVER).get_connection())
        else:
            dbbase.DBCore.conn = connection_str