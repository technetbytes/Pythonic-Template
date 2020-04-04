from sqlalchemy import create_engine
from db import connection
from  utilities import constant
import pandas as pd

class mssql_db:
    def __init__(self, connection_str):
        if connection_str is None:
            self.conn_str = connection.connection_string(constant.DB_TYPE_MSSQL_SERVER).get_connection()
        else:
            self.conn_str = connection_str

    def get_engine():
        return create_engine(self.conn_str)

    def get_connection():
        return get_engine().connect()