import mysql.connector
from mysql.connector import errorcode
import configparser
import pathlib

class DBConn:
    
    def __init__(self, config_file="config.ini"):
        self.config_file = config_file
        if self.config_file:
            # Crear una instancia de ConfigParser
            config = configparser.ConfigParser()
            # Configurar la ruta
            config_path = pathlib.Path(__file__).parent.absolute() / self.config_file
            # Leer el archivo
            config.read(config_path)
            # Definir una variable db_config que contiene los datos de la sección [database] del archivo.
            self.db_config = config['database']

    def get_data_base_name(self):
        return self.db_config.get('database')
    
    def connect_to_mysql(self):
        # Conectar a una base de datos MySQL Server
        try:
            connection = mysql.connector.connect(
                user=self.db_config.get('user'),
                password=self.db_config.get('password'),
                host=self.db_config.get('host'),
                database=self.db_config.get('database')  # Añadimos la base de datos aquí también
            )
            return connection
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise ("Usuario o Password no válido")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise ("La base de datos no existe.")
            else:
                print(err)
        return None

if __name__ == "__main__":
    db_conn = DBConn()
    connection = db_conn.connect_to_mysql()
    if connection:
        print("Conexión exitosa a la base de datos:", db_conn.get_data_base_name())
        connection.close()
