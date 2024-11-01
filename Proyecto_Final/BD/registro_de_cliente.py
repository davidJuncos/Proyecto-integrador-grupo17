# registro_de_cliente.py
from db_conn import DBConn
from mysql.connector import Error 
from rich.console import Console
from rich.table import Table

class Cliente:
    
    def __init__(self, connection=None):
        self.connection = connection or DBConn().connect_to_mysql()
        self.console = Console() 
    def registrar_cliente(self, dni, nombre, apellido, direccion, email, numeroTelefono):
        if not self.connection:
            raise ConnectionError("No se pudo establecer una conexión a la base de datos.")
        try:
            with self.connection.cursor() as cursor:
                query = """
                    INSERT INTO cliente (dni, nombre, apellido, direccion, email, numeroTelefono)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """  # Corrección de sintaxis en SQL
                values = (dni, nombre, apellido, direccion, email, numeroTelefono)
                cursor.execute(query, values)
                self.connection.commit()
        except Error as err:
            self.connection.rollback()
            raise Exception(f"Error al registrar cliente: {err}")
    
    def buscar_cliente_por_dni(self, dni):
        if not self.connection:
            raise ConnectionError("No se pudo establecer una conexión a la base de datos.")
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                query = """SELECT * FROM cliente WHERE dni = %s"""  
                cursor.execute(query, (dni,))
                return cursor.fetchone()
        except Error as err:
            raise Exception(f"Error al buscar cliente por DNI: {err}")

    def mostrar_cliente(self, cliente_info):
        """Muestra la información del cliente en formato tabla con rich."""
        table = Table(title="Información del Cliente")

        # Definir las columnas de la tabla
        table.add_column("ID", justify="center", style="cyan")
        table.add_column("DNI", justify="center", style="cyan")
        table.add_column("Nombre", justify="center", style="cyan")
        table.add_column("Apellido", justify="center", style="cyan")
        table.add_column("Dirección", justify="center", style="cyan")
        table.add_column("Email", justify="center", style="cyan")
        table.add_column("Teléfono", justify="center", style="cyan")

        # Agregar los datos del cliente a la tabla
        table.add_row(
            str(cliente_info['id']),
            cliente_info['dni'],
            cliente_info['nombre'],
            cliente_info['apellido'],
            cliente_info['direccion'],
            cliente_info['email'],
            cliente_info['numeroTelefono'],
        )

        # Mostrar la tabla
        self.console.print(table)
