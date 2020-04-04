import configparser
from utilities import constant
from config import configuration

class CacheConfiguration(configuration.Configuration):

    @property
    def host(self):
        return self.get_section(constant.CONFIG_SECTION_CACHE)[constant.CACHE_HOST]

    @property
    def port(self):
        return self.get_section(constant.CONFIG_SECTION_CACHE)[constant.CACHE_PORT]

    @property
    def password(self):
        return self.get_section(constant.CONFIG_SECTION_CACHE)[constant.CACHE_PASSWORD]