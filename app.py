from config import configuration
from config import database
from db import mssql
import pandas as pd
from assets import file_storage
from cache import data_cache 
from bridge.databse_bridge import DbBridge

'''Get configuration data from the .resource/config.ini file'''

# use configuration class get DATABASE Section from ini file
#config = configuration.Configuration(None)
# db_config = config.get_section("DATABASE")
# print(db_config['HOST'])

# use DatabaseConfiguration class user directly get DATABASE host using property
#ds = database.DatabaseConfiguration(None)
# print(ds.host)

'''Insert & Get record in the database'''

#obj_sql = mssql.MsSqlDb(None)

# conn = obj_sql.get_connection()
# data = pd.read_sql_query("select top 1 * from [knowHow].[dbo].[tModels]", conn)
# print(data)

# data2 = obj_sql.get_data("select top 1 * from [knowHow].[dbo].[tModels]")
# print(data2)

#obj_sql.insert_data("INSERT INTO KnowHow.dbo.tModels (Name, ModelName, Description, CreatedBy, CreatedOn, ModifiedBy, ModifiedOn, IsActive, CategoryId) VALUES('test1', 'test-1', 'test1 desc', 10, getdate(), NULL, '', 0, 1);")

'''Set & Read data in the cloud storage'''

#file_manager = file_storage.FileManager(None)
#file_manager.load_config()

#file_manager.upload_file("/home/saqib/Pictures/ijmal.png","ijmalbhai")

#s = file_manager.get_file_url("ijmalbhai")
#print(s)

#img = file_manager.get_image("https://res.cloudinary.com/dnbcbz9eu/image/upload/v1586115769/ijmalbhai.png")
#print(img)

'''Set & Read data in the cache'''

#redis_cache = data_cache.DataDeposit(None)
#redis_cache.load_config()
#redis_cache.set_item("Afa","Hello world")
#print(redis_cache.get_item("Afa"))

def main():
    direct_db()
    orm_model_call()

def direct_db():
    print("Direct database call ...")
    bridge = DbBridge()
    print(bridge.get_application())
    bridge.load_db()
    print(bridge.get_data("select top 1 * from [knowHow].[dbo].[tModels]"))

def orm_model_call():
    print("ORM mapper call ...")
    bridge = DbBridge()
    bridge.load_db()
    from models import projects
    projects = bridge.get_data_forModel(projects.Project)
    print('\n### All Projects:')
    for prj in projects:
        print(f'project id {prj.id} with keys {prj.webKey} and {prj.mobileKey}')
    print("done")
    
if __name__ == "__main__":
    print("Start Pythonic-Template Application")
    main()
    print("End Pythonic-Template Application")