from sqlalchemy import create_engine
from db import connection
from  utilities import constant
import pandas as pd

class mssql_db:
    '''This core class provide supporting function (CRUD Operations) for MS SQL Server.'''    
    def __init__(self, connection_str):
        if connection_str is None:
            self.conn_str = connection.connection_string(constant.DB_TYPE_MSSQL_SERVER).get_connection()
        else:
            self.conn_str = connection_str

    def get_engine(self):
        return create_engine(self.conn_str)

    def get_connection(self):
        return self.get_engine().connect()

    def get_data(self, query):
        return pd.read_sql_query(query, self.get_connection())
    
    def insert_data(self, insert_query):
        self.get_connection().execute(insert_query)
    
    def update_data(self, update_query):
        self.get_connection().execute(update_query)
    
    def delete_data(self, delete_query):
        self.get_connection().execute(delete_query)