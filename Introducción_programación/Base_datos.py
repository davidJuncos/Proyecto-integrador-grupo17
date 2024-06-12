import mysql.connector

HOST = "localhost"
USER = "root"
PASSWORD = "Logitech1."
BD = "hoteles"#nacidos

# Conectarse a la base de datos
conn = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=BD
)

# Crear un cursor
cursor = conn.cursor()

print(conn)

def cerrarConexion():
    cursor.close()
    conn.close()
    