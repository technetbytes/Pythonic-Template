
import unittest
from cache import data_cache 

def load_config():
    storage = data_cache.datadeposit(None).load_config()
    if storage is None:
        return False
    else:
        return True

class CacheTest(unittest.TestCase):
    '''This is Cache Test Class'''

    def test_loadconfig(self):
        self.assertEqual(load_config(), True)


if __name__ == '__main__':
    unittest.main()