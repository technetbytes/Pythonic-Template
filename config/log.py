import configparser
from utilities import constant
from config import configuration

class DatabaseConfiguration(configuration.Configuration):
    
    @property
    def log(self):
        return self.get_section(constant.CONFIG_SECTION_LOG)[constant.LOG_INFO]

    @property
    def error(self):
        return self.get_section(constant.CONFIG_SECTION_LOG)[constant.LOG_ERRORS]
