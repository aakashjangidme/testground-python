
import pymysql as msql
import logging
import sys
import pandas as pd
import app as app
from flask import current_app as app


# Join log
# Get logger instance
logger = logging.getLogger(__name__)
# Specify the output format
formatter = logging.Formatter('%(asctime)s\
              %(levelname)-8s:%(message)s')
# File log
file_handler = logging.FileHandler("logs/operation_database.log")
file_handler.setFormatter(formatter)
# Console log
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# Add specific log processor for logge
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.setLevel(logging.INFO)


class Dbclient:
    def __init__(self):
        self.DB_CONFIG = app.config['DB_CONFIG'] 
        print(self.DB_CONFIG)
        self.host = self.DB_CONFIG['host']
        self.user = self.DB_CONFIG['user']
        self.passw = self.DB_CONFIG['pass']
        self.port =self. DB_CONFIG['port']
        self.db = self.DB_CONFIG['db']
        self.charset = 'utf8'
        self.conn = None
        self.curr = None


    def __connect__(self):
        try:
            self.conn = msql.connect(
              host = self.host, user =  self.user, passwd =  self.passw, db =   self.db, port =  self.port, charset=self.charset)
            self.curr = self.conn.cursor()

        except Exception as e:
            logger.error("Conenction Failed : " + str(e))
            return False

    def __disconnect__(self):
        if self.conn:
            self.conn.close()
        return True

    def execute(self, sql):
        self.__connect__()
        try:
            if self.conn and self.curr:
                self.curr.execute(sql)
                self.conn.commit()
                return True
        except:
            logger.error("execution failed : " + sql)
            return False
        finally:
            self.__disconnect__()

    def fetch(self, sql):
        self.__connect__()
        try:
            if self.conn and self.curr:
                res = pd.read_sql(sql, con=self.conn)
                return res

        except Exception as e:
            logger.error("execution failed : " + sql)

            logger.info(e)

        finally:
            self.__disconnect__()

    def __str__(self):
        return 'db_client'
  

