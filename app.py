from config import configuration
from config import database

# use configuration class get DATABASE Section from ini file
config = configuration.Configuration(None)
db_config = config.get_section("DATABASE")
print(db_config['HOST'])

# use DatabaseConfiguration class user directly get DATABASE host using property
ds = database.DatabaseConfiguration(None)
print(ds.host)
