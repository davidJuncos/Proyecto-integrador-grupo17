import Base_datos

def agregar_reserva():
    try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return
        FechaEntrada = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        FechaSalida = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
        EstadoReseva = int(input("Ingrese el estado de su reserva (1 - 0): "))
        idPersona = int(input("Ingrese ID del personal: "))
        DNI = int(input("Ingrese DNI del cliente: "))
        NroHabitacion = int(input("Ingrese el número de la habitación: "))
        
        query = "INSERT INTO Reservas (FechaEntrada, FechaSalida, EstadoReserva, idPersonal, DNI,  NroHabitacion) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (FechaEntrada, FechaSalida, EstadoReseva, idPersona, DNI, NroHabitacion)
        
        Base_datos.cursor.execute(query, values)
        Base_datos.conn.commit()
        print("Reserva agregada con éxito.")
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al agregar reserva: {error}")


def modificar_reserva():
    try:
        if not Base_datos.conn.is_connected():
            print("La conexión a la Base de Datos no está activa")
            return

        idReserva = input("Ingrese el ID de la reserva: ")
        query = "SELECT * FROM reservas WHERE idReserva = %s"
        values = (idReserva,)
        Base_datos.cursor.execute(query, values)
        reserva = Base_datos.cursor.fetchone()

        if not reserva:
            print(f"No existe una persona que haya reserva con ID: {idReserva}")
            return

        print("Información actual de la reserva:")
        print(f"fechaEntrada: {reserva[1]}")
        print(f"fechaSalida: {reserva[2]}")
        print(f"estadoReserva: {reserva[3]}")
        print(f"idReserva: {reserva[4]}")
        print(f"dni: {reserva[5]}")
        print(f"numeroHabitacion: {reserva[6]}")

        fechaEntrada = input("Ingrese la nueva fecha de entrada (YYYY-MM-DD, o presione Enter para mantener la actual): ")
        fechaSalida = input("Ingrese la nueva fecha de salida (YYYY-MM-DD, o presione Enter para mantener la actual): ")
        estadoReserva = input("Ingrese el nuevo estado (o presione Enter para mantener el actual): ")
        idReserva = input("Ingrese el ID de la persona nueva (o presione Enter para mantener la actual): ")
        dni = input("Ingrese el nuevo DNI (o presione Enter para mantener el actual): ")
        numeroHabitacion = input("Ingrese el nuevo número de habitación (o presione Enter para mantener el actual): ")

        query = "UPDATE Reservas SET "
        update_values = []

        if fechaEntrada:
            query += "FechaEntrada = %s, "
            update_values.append(fechaEntrada)
        if fechaSalida:
            query += "FechaSalida = %s, "
            update_values.append(fechaSalida)
        if estadoReserva:
            query += "EstadoReserva = %s, "
            update_values.append(estadoReserva)
        if idReserva:
            query += "idReserva = %s, "
            update_values.append(idReserva)
        if dni:
            query += "DNI = %s, "
            update_values.append(dni)
        if numeroHabitacion:
            query += "NroHabitacion = %s, "
            update_values.append(numeroHabitacion)

        query = query.rstrip(", ")
        query += " WHERE idReserva = %s"
        update_values.append(fechaEntrada)

        Base_datos.cursor.execute(query, update_values)
        Base_datos.conn.commit()
        print("Reserva modificada con éxito.")
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al modificar reserva: {error}")
    

def eliminar_reserva():
    try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return

        idReserva = input("Ingrese el ID de la reserva que desea eliminar: ")
        query = "DELETE FROM Reservas WHERE idReserva = %s"
        values = (idReserva,)
        Base_datos.cursor.execute(query, values)
        Base_datos.conn.commit()

        if Base_datos.cursor.rowcount > 0:
            print(f"Reserva con ID {idReserva} eliminada con éxito.")
        else:
            print(f"No se encontró ninguna reserva con el ID {idReserva}.")
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al eliminar reserva: {error}")


def mostrar_reserva():
    try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return

        idReserva = input("Ingrese el ID de la reserva que desea mostrar (o presione Enter para mostrar todas): ")
        if idReserva:
            query = "SELECT * FROM Reservas WHERE idReserva = %s"
            values = (idReserva,)
            Base_datos.cursor.execute(query, values)
            reserva = Base_datos.cursor.fetchone()
            if reserva:
                print(f"Fecha de entrada: {reserva[1]}")
                print(f"Fecha de salida: {reserva[2]}")
                print(f"Estado de reserva: {reserva[3]}")
                print(f"idReserva: {reserva[4]}")
                print(f"DNI: {reserva[5]}")
                print(f"Número de habitación: {[6]}")
            else:
                print(f"No se encontró ninguna reserva con el ID {idReserva}.")
        else:
            query = "SELECT * FROM Reservas"
            Base_datos.cursor.execute(query)
            reservas = Base_datos.cursor.fetchall()
            for reserva in reservas:
                print(reserva)
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al mostrar reserva(s): {error}")

def mostrar_reserva_completa():
    try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return False

        query = "SELECT * FROM reservas"
        Base_datos.cursor.execute(query)
        reserva = Base_datos.cursor.fetchall()

        if reserva:
            for i in reserva:
                print(i)
            return True
        else:
            print("No hay reserva en la base de datos.")
            return False
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al mostrar agenda completa: {error}")
        return False

