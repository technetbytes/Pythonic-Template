import configparser
from utilities import constant
from config import configuration

class ApplicationConfiguration(configuration.Configuration):
    '''Using this class we load application configuration parameters'''
    
    @property
    def envirnoment(self):
        return self.get_section(constant.CONFIG_SECTION_APP)[constant.APP_ENVIRONMENT]

    @property
    def debug(self):
        return self.get_section(constant.CONFIG_SECTION_APP)[constant.APP_DEBUG]

    @property
    def database(self):
        return self.get_section(constant.CONFIG_SECTION_APP)[constant.APP_DATABASE]