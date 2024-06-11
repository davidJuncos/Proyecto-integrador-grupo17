import Base_datos
from roles import mostrar_roles

def agregar_personal():
    try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return

        Nombre = input("Ingrese nombre: ")
        Apellido = input("Ingrese apellido: ")
        
        while True:
            try:
                Horainicia = float(input("Ingrese horario de inicio (formato 24h, ej. 9.5 para 9:30): "))
                HoraFin = float(input("Ingrese horario de salida (formato 24h, ej. 17.0 para 17:00): "))
                break
            except ValueError:
                print("Por favor ingrese una hora válida en formato decimal.")

        if not mostrar_roles():
            return  # Si no hay roles, no continuar

        IdRol = input("Ingrese Id del rol: ")

        query = "INSERT INTO Personal (Nombre, Apellido, HoraInicia, HoraFin, Estado, IdRol) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (Nombre, Apellido, Horainicia, HoraFin, 1, IdRol)
        
        Base_datos.cursor.execute(query, values)
        Base_datos.conn.commit()
        print("Personal insertado con éxito.")
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al agregar personal: {error}")

def modificar_personal():
    try:
        if not Base_datos.conn.is_connected():
            print("La conexión a la Base de Datos no está activa")
            return False

        id_personal = input("Ingrese el ID del personal que desea modificar: ")
        query = "SELECT * FROM Personal WHERE idPersonal = %s"
        values = (id_personal,)
        Base_datos.cursor.execute(query, values)
        persona = Base_datos.cursor.fetchone()

        if not persona:
            print(f"No existe en la base de datos la persona con ID: {id_personal}")
            return False

        # Mostrar información actual del personal
        print("Información actual del personal:")
        print(f"Nombre: {persona[1]}")
        print(f"Apellido: {persona[2]}")
        print(f"Horario de Inicio: {persona[3]}")
        print(f"Horario de Fin: {persona[4]}")
        print(f"ID Rol: {persona[6]}")

        # Solicitar información actualizada del personal
        nombre = input("Ingrese el nuevo nombre (o presione Enter para mantener el actual): ")
        apellido = input("Ingrese el nuevo apellido (o presione Enter para mantener el actual): ")
        hora_inicio = input("Ingrese el nuevo horario de inicio (formato 24h, ej. 9.5 para 9:30, o presione Enter para mantener el actual): ")
        hora_fin = input("Ingrese el nuevo horario de fin (formato 24h, ej. 17.0 para 17:00, o presione Enter para mantener el actual): ")
        id_rol = input("Ingrese el nuevo ID del Rol (o presione Enter para mantener el actual): ")

        # Construir la consulta de actualización
        query = "UPDATE Personal SET "
        update_values = []

        if nombre:
            query += "Nombre = %s, "
            update_values.append(nombre)
        if apellido:
            query += "Apellido = %s, "
            update_values.append(apellido)
        if hora_inicio:
            query += "HoraInicia = %s, "
            update_values.append(hora_inicio)
        if hora_fin:
            query += "HoraFin = %s, "
            update_values.append(hora_fin)
        if id_rol:
            query += "IdRol = %s, "
            update_values.append(id_rol)

        # Eliminar la última coma y espacio en la consulta
        query = query.rstrip(", ")
        query += " WHERE idPersonal = %s"
        update_values.append(id_personal)

        # Ejecutar la consulta de actualización
        Base_datos.cursor.execute(query, update_values)
        Base_datos.conn.commit()

        print("Personal modificado con éxito.")
        return True

    except Base_datos.mysql.connector.Error as error:
        print(f"Error al modificar personal: {error}")
        return False
    

def eliminar_personal():
    try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return

        idPersonal = input("Ingrese el ID del personal que desea eliminar: ")
        query = "DELETE FROM Personal WHERE idPersonal = %s"
        values = (idPersonal,)
        Base_datos.cursor.execute(query, values)
        Base_datos.conn.commit()

        if Base_datos.cursor.rowcount > 0:
            print(f"Personal con ID {idPersonal} eliminado con éxito.")
        else:
            print(f"No se encontró ninguna persona con el ID {idPersonal}.")
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al eliminar personal: {error}")

def mostrar_personal_unico():
    try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return False

        id_Personal = int(input("Ingrese el ID del personal: "))
        query = "SELECT * FROM Personal WHERE idPersonal = %s"
        values = (id_Personal,)
        Base_datos.cursor.execute(query, values)
        personaUnica = Base_datos.cursor.fetchone()
        #print(personaUnica)
        if personaUnica:
            print(f"Nombre: {personaUnica[1]}")
            print(f"Apellido: {personaUnica[2]}")
            print(f"Horario de Inicio: {personaUnica[3]}")
            print(f"Horario de Fin: {personaUnica[4]}")
            print(f"Estado: {personaUnica[5]}")
            print(f"ID Rol: {personaUnica[6]}")
            return True
        else:
            print(f"No existe en la base de datos la persona con id: {id_Personal}")
            return False
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al mostrar personal: {error}")
        return False

def mostrar_personal_completo():
    try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return False

        query = "SELECT * FROM Personal"
        Base_datos.cursor.execute(query)
        personal = Base_datos.cursor.fetchall()

        if personal:
            for persona in personal:
                print(persona)
            return True
        else:
            print("No hay personal en la base de datos.")
            return False
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al mostrar agenda completa: {error}")
        return False

