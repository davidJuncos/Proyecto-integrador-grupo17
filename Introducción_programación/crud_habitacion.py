import Base_datos
def agregar_habitacion ():
   try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return
        NroHabitacion = int(input("Ingrese el numero de habitacion: "))
        TipoHabitacion = input("Ingrese tipo de habitacion: ")
        IdDisponibilidad = input("Ingrese si esta disponible(1/0): ")
        
        while True:
            try:
                PrecioNoche = float(input("Ingrese el precio por noche (solo numeros): "))
                break
            except ValueError:
                print("Por favor ingrese una hora válida en formato decimal.")

        query = "INSERT INTO habitaciones (NroHabitacion, TipoHabitacion, PrecioNoche,IdDisponibilidad) VALUES (%s, %s, %s, %s)"
        values = (NroHabitacion, TipoHabitacion, PrecioNoche, IdDisponibilidad)
        
        Base_datos.cursor.execute(query, values)
        Base_datos.conn.commit()
        print("Habitacion insertado con éxito.")
   except Base_datos.mysql.connector.Error as error:
         print(f"Error al agregar habitacion: {error}")

def modificar_habitacion ():
    try:
        if not Base_datos.conn.is_connected():
            print("La conexión a la Base de Datos no está activa")
            return False

        num_habitacion = input("Ingrese el numero de la habitacion que desea modificar: ")
        query = "SELECT * FROM habitaciones WHERE NroHabitacion = %s"
        values = (num_habitacion,)
        Base_datos.cursor.execute(query, values)
        habitacion = Base_datos.cursor.fetchone()

        if not habitacion:
            print(f"No existe en la base de datos la persona con ID: {num_habitacion}")
            return False

        # Mostrar información actual del personal
        print("Información actual del personal:")
        print(f"Tipo de habitacion: {habitacion[1]}")
        print(f"Precio de la noche: {habitacion[2]}")
        print(f"Disponibilidad: {habitacion[3]}")

        # Solicitar información actualizada del personal
        Tipo_habitacion = input("Ingrese el nuevo tipo de habitacion (o presione Enter para mantener el actual): ")
        Precio_noche = input("Ingrese el nuevo precio por noche (o presione Enter para mantener el actual): ")
        id_disponibilidad = input("Ingrese la nueva disponbilidad (o presione Enter para mantener el actual): ")
        
        # Construir la consulta de actualización
        query = "UPDATE habitaciones SET "
        update_values = []

        if Tipo_habitacion:
            query += "TipoHabitacion = %s, "
            update_values.append(Tipo_habitacion)
        if Precio_noche:
            query += "PrecioNoche = %s, "
            update_values.append(Precio_noche)
        if id_disponibilidad:
            query += "IdDisponibilidad = %s, "
            update_values.append(id_disponibilidad)

        # Eliminar la última coma y espacio en la consulta
        query = query.rstrip(", ")
        query += " WHERE NroHabitacion = %s"
        update_values.append(num_habitacion)

        # Ejecutar la consulta de actualización
        Base_datos.cursor.execute(query, update_values)
        Base_datos.conn.commit()

        print("Habitacion modificada con éxito.")
        return True

    except Base_datos.mysql.connector.Error as error:
        print(f"Error al modificar habitacion: {error}")
        return False
    
def eliminar_habitacion ():
    try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return

        num_habitacion = input("Ingrese el numero de habitacion que desea eliminar: ")
        query = "DELETE FROM habitaciones WHERE NroHabitacion = %s"
        values = (num_habitacion,)
        Base_datos.cursor.execute(query, values)
        Base_datos.conn.commit()

        if Base_datos.cursor.rowcount > 0:
            print(f"La habitacion {num_habitacion} eliminada con éxito.")
        else:
            print(f"No se encontró ninguna habitacion con el numero {num_habitacion}.")
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al eliminar habitacion: {error}")




def mostrar_todas_habitaciones():
    try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return False

        query = "SELECT * FROM habitaciones"
        Base_datos.cursor.execute(query)
        habitacion = Base_datos.cursor.fetchall()

        if habitacion:
            for i in habitacion:
                print(i)
            return True
        else:
            print("No hay habitaciones en la base de datos.")
            return False
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al mostrar agenda completa: {error}")
        return False
    
    
def mostrar_habitacion_unica():
    try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return False

        NumHabitacion= int(input("Ingrese el numero de habitacion: "))
        query = "SELECT * FROM habitaciones WHERE NroHabitacion = %s"
        values = (NumHabitacion,)
        Base_datos.cursor.execute(query, values)
        Habitacion_Unica = Base_datos.cursor.fetchone()
        #print(personaUnica)
        if Habitacion_Unica:
            print(f"Tipo de habitacion: {Habitacion_Unica[1]}")
            print(f"Precio noche: {Habitacion_Unica[2]}")
            print(f"Disponibilidad: {Habitacion_Unica[3]}")
            return True
        else:
            print(f"No existe en la base de datos la habitacion numero: {NumHabitacion}")
            return False
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al mostrar Habitacion: {error}")
        return False
