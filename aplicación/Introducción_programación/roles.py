import Base_datos
def mostrar_roles():
    try:
        if not Base_datos.conn.is_connected():
            print("Conexión no está activa")
            return False
        
        query = "SELECT * FROM Roles"
        Base_datos.cursor.execute(query)
        roles = Base_datos.cursor.fetchall()

        if roles:
            for role in roles:
                print(role)
            print(f"{len(roles)} Filas afectadas")
            return True
        else:
            print(f"No existe en la base de datos roles del personal")
            return False
    except Base_datos.mysql.connector.Error as error:
        print(f"Error al ejecutar la consulta: {error}")
        return False