from config import configuration
from config import database
from db import mssql
import pandas as pd
from assets import file_storage
from cache import data_cache 

# use configuration class get DATABASE Section from ini file
# config = configuration.Configuration(None)
# db_config = config.get_section("DATABASE")
# print(db_config['HOST'])

# use DatabaseConfiguration class user directly get DATABASE host using property
# ds = database.DatabaseConfiguration(None)
# print(ds.host)


#obj_sql = mssql.mssql_db(None)

# conn = obj_sql.get_connection()
# data = pd.read_sql_query("select top 1 * from [knowHow].[dbo].[tModels]", conn)
# print(data)

# data2 = obj_sql.get_data("select top 1 * from [knowHow].[dbo].[tModels]")
# print(data2)

#obj_sql.insert_data("INSERT INTO KnowHow.dbo.tModels (Name, ModelName, Description, CreatedBy, CreatedOn, ModifiedBy, ModifiedOn, IsActive, CategoryId) VALUES('test1', 'test-1', 'test1 desc', 10, getdate(), NULL, '', 0, 1);")

#storage = file_storage.file_manager(None)
#storage.load_config()

#storage.upload_file("/home/saqib/Pictures/ijmal.png","ijmalbhai")

#s = storage.get_file_url("ijmalbhai")
#print(s)

#img = storage.get_image("https://res.cloudinary.com/dnbcbz9eu/image/upload/v1586115769/ijmalbhai.png")
#print(img)

redis_cache = data_cache.datadeposit(None)
redis_cache.load_config()
redis_cache.set_item("Afa","Hello world")
print(redis_cache.get_item("Afa"))