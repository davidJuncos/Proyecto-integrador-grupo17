# informes.py
from db_conn import DBConn
from mysql.connector import Error
from rich.console import Console
from rich.table import Table
class Informe:

    def __init__(self, connection=None):
        self.connection = connection or DBConn().connect_to_mysql()
from rich.console import Console
from rich.table import Table

class Informe:

    def __init__(self, connection=None):
        self.connection = connection or DBConn().connect_to_mysql()

    def generar_informe_reservas_activas(self):
        if not self.connection:
            raise ConnectionError("No se pudo establecer una conexión a la base de datos.")
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                query = """
                    SELECT r.id, c.nombre, c.apellido, h.numeroHabitacion, r.fechaEntrada, r.fechaSalida
                    FROM reserva r
                    JOIN cliente c ON r.idCliente = c.id
                    JOIN habitacion h ON r.idHabitacion = h.id
                    WHERE r.estadoReserva = 'activa'
                """
                cursor.execute(query)
                reservas = cursor.fetchall()

                # Crear la tabla usando Rich
                table = Table(title="Informe de Reservas Activas")

                # Definir las columnas de la tabla
                table.add_column("ID Reserva", justify="center")
                table.add_column("Nombre Cliente", justify="center")
                table.add_column("Apellido Cliente", justify="center")
                table.add_column("Habitación", justify="center")
                table.add_column("Fecha Entrada", justify="center", style="red")
                table.add_column("Fecha Salida", justify="center", style="green")

                # Llenar la tabla con los datos
                for reserva in reservas:
                    table.add_row(
                        str(reserva['id']),
                        reserva['nombre'],
                        reserva['apellido'],
                        str(reserva['numeroHabitacion']),
                        reserva['fechaEntrada'].strftime('%Y-%m-%d'),  # Formatear fecha
                        reserva['fechaSalida'].strftime('%Y-%m-%d')  # Formatear fecha
                    )

                # Imprimir la tabla
                console = Console()
                console.print(table)

        except Error as err:
            raise Exception(f"Error al generar el informe de reservas activas: {err}")


    def generar_informe_mantenimientos(self):
        if not self.connection:
            raise ConnectionError("No se pudo establecer una conexión a la base de datos.")
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                query = """
                    SELECT h.numeroHabitacion, e.estado, m.fechaReporte, m.fechaResolucion, 
                    m.descripcionProblema, m.costo, p.nombre AS nombrePersonal, p.apellido AS apellidoPersonal
                    FROM mantenimiento m
                    JOIN habitacion h ON m.idHabitacion = h.id
                    JOIN estadoMantenimiento e ON m.idEstadoMantenimiento = e.id
                    JOIN personal p ON m.idPersonal = p.id
                    ORDER BY m.fechaReporte DESC
                """
                cursor.execute(query)
                mantenimientos = cursor.fetchall()
                
                # Crear la tabla usando Rich
                table = Table(title="Informe de Mantenimientos")

                # Definir las columnas de la tabla
                table.add_column("Habitación", justify="center")
                table.add_column("Estado", justify="center", style="yellow")
                table.add_column("Fecha Reporte", justify="center", style="red")
                table.add_column("Fecha Resolución", justify="center", style="green")
                table.add_column("Descripción Problema", justify="center")
                table.add_column("Costo", justify="center")
                table.add_column("Personal a Cargo", justify="center")

                # Llenar la tabla con los datos
                for mantenimiento in mantenimientos:
                    table.add_row(
                        str(mantenimiento['numeroHabitacion']),
                        mantenimiento['estado'],
                        mantenimiento['fechaReporte'].strftime('%Y-%m-%d'),  # Formatear fecha
                        mantenimiento['fechaResolucion'].strftime('%Y-%m-%d') if mantenimiento['fechaResolucion'] else "No resuelto",
                        mantenimiento['descripcionProblema'],
                        str(mantenimiento['costo']) if mantenimiento['costo'] is not None else "N/A",
                        f"{mantenimiento['nombrePersonal']} {mantenimiento['apellidoPersonal']}"
                    )

                # Imprimir la tabla
                console = Console()
                console.print(table)

        except Error as err:
            raise Exception(f"Error al generar el informe de mantenimientos: {err}")
