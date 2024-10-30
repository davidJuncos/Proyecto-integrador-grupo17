import mysql.connector
from mysql.connector import errorcode
import configparser
import pathlib

class DBConn:
    
    def __init__(self, config_file="config.ini"):
        self.config_file = config_file
        if self.config_file:
            config = configparser.ConfigParser()
            config_path = pathlib.Path(__file__).parent.absolute() / self.config_file
            config.read(config_path)
            self.db_config = config['database']

    def get_data_base_name(self):
        return self.db_config.get('database')
    
    def connect_to_mysql(self):
        try:
            connection = mysql.connector.connect(
                user=self.db_config.get('user'),
                password=self.db_config.get('password'),
                host=self.db_config.get('host'),
                database=self.db_config.get('database')
            )
            return connection
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise Exception("Usuario o Password no válido")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise Exception("La base de datos no existe.")
            else:
                raise Exception(f"Error inesperado: {err}")