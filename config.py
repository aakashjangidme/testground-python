success = "success"
failed = "failed"
gen_err = "something went wrong."


import logging, os


class Config(object):
    DEBUG = False
    TESTING = False
    HOST = os.getenv('APP_HOST')    
    PORT = int(os.getenv('APP_PORT', 3000)) 
    SECRET = 'default'
    
    DB_CONFIG = {
    "host": os.getenv('RDS_HOST'),
    "port": int(os.getenv('RDS_PORT', 3300)),
    "user": os.getenv('RDS_USER'),
    "pass":  os.getenv('RDS_PASS'),
    "db": os.getenv('RDS_DB'),
    "charset": 'utf8'
    } 

class TestConfig(Config):
    DEBUG = False
    TESTING = True
    SECRET = 'test-secret-key'


class DevConfig(Config):
    DEBUG = True
    TESTING = False
    SECRET = 'dev-secret-key'

    DB_CONFIG = {
    "host": os.getenv('DB_HOST', 'localhost'),
    "port": int(os.getenv('DB_PORT', 3300)),
    "user": os.getenv('DB_USER'),
    "pass":  os.getenv('DB_PASS'),
    "db": os.getenv('DB'),
    "charset": 'utf8'
    }  


class ProdConfig(Config):
    SECRET = 'prod-secret-key'
    pass


logging.basicConfig(
filename=os.getenv("SERVICE_LOG", "logs/server.log"),
level=logging.DEBUG,
format="%(levelname)s: %(asctime)s \
    pid:%(process)s module:%(module)s %(message)s",
datefmt="%d/%m/%y %H:%M:%S",
)
