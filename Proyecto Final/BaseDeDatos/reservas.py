# reservas.py
from db_conn import DBConn
from mysql.connector import Error

class Reserva:
    
    def __init__(self, connection=None):
        self.connection = connection or DBConn().connect_to_mysql()
        
    def hacer_reserva(self, idPersonal, idHabitacion, idCliente, fechaEntrada, fechaSalida):
        if not self.connection:
            raise ConnectionError("No se pudo establecer una conexión a la base de datos.")
        try:
            with self.connection.cursor() as cursor:
                query = """ 
                    INSERT INTO reserva (idPersonal, idHabitacion, idCliente, fechaEntrada, fechaSalida)
                    VALUES (%s, %s, %s, %s, %s)
                """  # Corrección de sintaxis en SQL
                values = (idPersonal, idHabitacion, idCliente, fechaEntrada, fechaSalida)
                cursor.execute(query, values)
                self.connection.commit()
        except Error as err:
            self.connection.rollback()
            raise Exception(f"Error al hacer la reserva: {err}")
    
    def consultar_disponibilidad(self, fechaEntrada, fechaSalida):
        if not self.connection:
            raise ConnectionError("No se pudo establecer una conexión a la base de datos.")
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                query = """
                    SELECT h.numeroHabitacion, th.tipo, th.precioNoche
                    FROM habitacion h
                    JOIN tipoHabitacion th ON h.idTipoHabitacion = th.id
                    WHERE h.idDisponibilidad = (SELECT id FROM disponibilidad WHERE disponibilidad = 'Disponible')
                    AND h.id NOT IN (
                        SELECT idHabitacion FROM reserva 
                        WHERE (fechaEntrada BETWEEN %s AND %s) OR (fechaSalida BETWEEN %s AND %s)
                    )
                """
                cursor.execute(query, (fechaEntrada, fechaSalida, fechaEntrada, fechaSalida))
                return cursor.fetchall()
        except Error as err:
            raise Exception(f"Error al consultar la disponibilidad: {err}")
