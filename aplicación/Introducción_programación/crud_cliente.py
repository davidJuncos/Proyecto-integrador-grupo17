import Base_datos

def agregar_cliente():
    try:
        #verificacion de conexion de base de datos
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return
        
        while True:
            try:
                #se pide el ingreso de datos
                DNI = int(input("Ingrese DNI: "))
                break  # Si se puede convertir a entero, sal del bucle
            except ValueError:
                print("Por favor, ingrese un DNI válido.")
       
        Nombre = input("Ingrese nombre: ")
        Apellido = input("Ingrese apellido: ")
        Direccion = input("Ingrese Direccion: ")
        Email = input("Ingrese Email: ")
        NumeroTelefono = input("Ingrese Nro. de Telefono: ")

        #Se agrega la instrucción SQL donde se inserta el Cliente      
        query = "INSERT INTO Clientes (DNI, Nombre, Apellido, Direccion, Email, NumeroTelefono, Estado) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        #aca pasa los valores guardados en las variables a Values (variable)
        values = (DNI, Nombre, Apellido, Direccion, Email, NumeroTelefono, 1)
        
        Base_datos.cursor.execute(query, values)
        #ejecuta la instruccion SQL que se paso a la variable query , sus respectivos  valores 
        Base_datos.conn.commit()
        print("Cliente insertado con éxito.")
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al agregar cliente: {error}")

def modificar_cliente():
    try:
        if not Base_datos.conn.is_connected():
            print("La conexión a la Base de Datos no está activa")
            return False

        DNI = input("Ingrese el DNI del Cliente que desea modificar: ")
        query = "SELECT * FROM Clientes WHERE DNI = %s"
        values = (DNI,)
        Base_datos.cursor.execute(query, values)
        cliente = Base_datos.cursor.fetchone()

        if not cliente:
            print(f"No existe en la base de datos el cliente con DNI: {DNI}")
            return False

        # Mostrar información actual del cliente
        print("Información actual del cliente:")
        print(f"Nombre: {cliente[1]}")
        print(f"Apellido: {cliente[2]}")
        print(f"Dirección: {cliente[3]}")
        print(f"Email: {cliente[4]}")
        print(f"Nro. Telefono: {cliente[5]}")

        # Solicitar información actualizada del cliente
        nombre = input("Ingrese el nuevo nombre (o presione Enter para mantener el actual): ")
        apellido = input("Ingrese el nuevo apellido (o presione Enter para mantener el actual): ")
        Direccion = input("Ingrese la dirección, (o presione Enter para mantener el actual): ")
        Email = input("Ingrese el nuevo Email (o presione Enter para mantener el actual): ")
        NumeroTelefono = input("Ingrese el nuevo nro. de telefono (o presione Enter para mantener el actual): ")

        # Construir la consulta de actualización
        query = "UPDATE Clientes SET "
        update_values = []

        if nombre:
            query += "Nombre = %s, "
            update_values.append(nombre)
        if apellido:
            query += "Apellido = %s, "
            update_values.append(apellido)
        if Direccion:
            query += "Direccion = %s, "
            update_values.append(Direccion)
        if Email:
            query += "Email = %s, "
            update_values.append(Email)
        if NumeroTelefono:
            query += "NumeroTelefono = %s, "
            update_values.append(NumeroTelefono)

        # Eliminar la última coma y espacio en la consulta
        query = query.rstrip(", ")
        query += " WHERE DNI = %s"
        update_values.append(DNI)

        # Ejecutar la consulta de actualización
        Base_datos.cursor.execute(query, update_values)
        Base_datos.conn.commit()

        print("Cliente modificado con éxito.")
        return True

    except Base_datos.mysql.connector.Error as error:
        print(f"Error al modificar cliente: {error}")
        return False

def eliminar_cliente():
    try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return

        DNI = input("Ingrese el DNI del cliente que desea eliminar: ")
        query = "DELETE FROM Clientes WHERE DNI = %s"
        values = (DNI,)
        Base_datos.cursor.execute(query, values)
        Base_datos.conn.commit()

        if Base_datos.cursor.rowcount > 0:
            print(f"Cliente con DNI {DNI} eliminado con éxito.")
        else:
            print(f"No se encontró ninguna cliente con el DNI {DNI}.")
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al eliminar cliente: {error}")

def mostrar_un_cliente():
    try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return False

        DNI = int(input("Ingrese el DNI del cliente: "))
        query = "SELECT * FROM Clientes WHERE DNI = %s"
        values = (DNI,)
        Base_datos.cursor.execute(query, values)
        clienteUnico = Base_datos.cursor.fetchone()
        
        if clienteUnico:
            print(f"Nombre: {clienteUnico[1]}")
            print(f"Apellido: {clienteUnico[2]}")
            print(f"Dirección: {clienteUnico[3]}")
            print(f"Email: {clienteUnico[4]}")
            print(f"Nro. de Telefono: {clienteUnico[5]}")
            return True
        else:
            print(f"No existe en la base de datos del cliente con DNI: {DNI}")
            return False
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al mostrar cliente: {error}")
        return False

def mostrar_clientes_completo():
    try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return False

        query = "SELECT * FROM Clientes"
        Base_datos.cursor.execute(query)
        client = Base_datos.cursor.fetchall()

        if client:
            for cliente in client:
                print(cliente)
            return True
        else:
            print("No hay clientes en la base de datos.")
            return False

    except Base_datos.mysql.connector.Error as error:
        print(f"Error al mostrar clientes completos: {error}")
        return False
