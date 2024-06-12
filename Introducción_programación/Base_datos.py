
import mysql.connector 

HOST = "LocalHost"
USER = "root"
PASSWORD = "Logitech1."
BD = "hoteles"

try:
    # Conectarse a la base de datos
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=BD
    )

    if conn.is_connected():
        print("Conexión exitosa a la base de datos.")
    else:
        print("No se pudo conectar a la base de datos.")

    # Crear un cursor
    cursor = conn.cursor()

except mysql.connector.Error as error:
    print("Error al conectarse a la base de datos: {}".format(error))

finally:
    # Cerrar el cursor y la conexión
    """
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexión cerrada.")"""