import unittest
from db import mssql

def connect_mssql():
    obj_sql = mssql.mssql_db(None)
    conn = obj_sql.get_connection
    if conn is None:
        return False
    else:
        return True

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(connect_mssql(), True)